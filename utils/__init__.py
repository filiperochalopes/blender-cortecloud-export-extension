import bpy, os, re

# Configurações de ambiente para melhor uso em móveis e precisão
def configure_environment(context):
    unit_settings = bpy.context.scene.unit_settings
    unit_settings.system = 'METRIC'
    unit_settings.scale_length = 0.001
    unit_settings.length_unit = 'MILLIMETERS'
    unit_settings.system_rotation = 'DEGREES'
    # Cada cena é composta de várias áreas/janelas
    areas = [a for a in bpy.context.screen.areas if a.type == 'VIEW_3D']
    # spaces = [s for s in areas if s.type == 'VIEW_3D']
    # workspace = None
    for area in areas:
        for s in area.spaces:
            if s.type == 'VIEW_3D':
                s.shading.type = 'SOLID'
                s.shading.show_xray = True
                s.overlay.grid_scale = 0.001
                s.clip_end = 1000000

    # Alterando o clipping point da camera ativa, caso exista uma
    if bpy.context.scene.camera:
        bpy.context.scene.camera.data.clip_end = 1000000

    # Removendo todas as luzes e câmeras do ambiente
    for obj in bpy.context.scene.objects:
        if obj.type == 'LIGHT' or obj.type == 'CAMERA':
            bpy.data.objects.remove(obj, do_unlink=True)
            
    # Atualizando para correção de medidas em script em relação ao viewport
    bpy.context.view_layer.update()


def create_default_materials(context):
    # Função para criar material se não existir
    def create_material(name, color):
        if name not in bpy.data.materials:
            mat = bpy.data.materials.new(name=name)
            mat.diffuse_color = color
            print(f"Material {name} criado.")
        else:
            print(f"Material {name} já existe.")

    # Criando materiais iniciais para MDFs brancos
    create_material('MDF Branco', (0.905, 0.905, 0.905, 1))  # #E7E7E7
    create_material('L1 Branco', (0, 0.905, 0.890, 1))       # #00E7E3
    create_material('L2 Branco', (0, 0.905, 0.890, 1))       # #00E7E3
    create_material('C1 Branco', (0, 0.905, 0.890, 1))       # #00E7E3
    create_material('C2 Branco', (0, 0.905, 0.890, 1))       # #00E7E3
    create_material('Sem Fita', (0.866, 0, 0.905, 1))        # #DD00E7

    # Atualizando para correção de medidas em script em relação ao viewport
    bpy.context.view_layer.update()



def export_to_csv(filepath):
    # Captura apenas a seleção, gosto de utilizar coleções de madeira e outras de outros materiais, dessa forma fica fácil selecionar apenas os itens de madeira
    selection = bpy.context.selected_objects

    # Arquivo de saída (edite aqui)
    output_file = filepath
    # lista de nome de objetos que não deverão ser analisados, pois são duplicatas de outros objetos. São esses os de final *.001, *.002 ...
    blacklist = []


    # classe para organizar a fitagem de borda de uma peça
    class EdgeTapes:
        def __init__(self, material_names):
            def get_tape_material(tape_identifier: str):
                l = [m for m in material_names if tape_identifier in m]
                return l[0].replace(tape_identifier, "").strip() if len(l) > 0 else None

            # Verifica se existem algum material com as palavras chaves
            self.c1 = get_tape_material("C1")
            self.c2 = get_tape_material("C2")
            self.l1 = get_tape_material("L1")
            self.l2 = get_tape_material("L2")

        def __str__(self):
            str = ""
            if self.c1:
                str += f"C1: {self.c1} "
            if self.c2:
                str += f"C2: {self.c2} "
            if self.l1:
                str += f"L1: {self.l1} "
            if self.l2:
                str += f"L2: {self.l2} "
            return str


    # classe para organizar as características de um corte do material
    class WoodenPiece:
        def __init__(
            self,
            dimensions: list,
            material_names: list,
            name: str = None,
            role: str = None,
        ):
            self.name = name
            self.role = role
            self.thickness = min(dimensions)
            dimensions.remove(self.thickness)
            self.width = dimensions[0]
            self.height = dimensions[1]
            self.material = self.get_main_material_from_materials(material_names)
            self.edge_tapes = EdgeTapes(material_names)

        def get_main_material_from_materials(self, material_names):
            for m in material_names:
                if re.search("^((?!C1|C2|L1|L2|Fita).)*$", m):
                    return f"{m} {self.thickness}mm"
            return None

        def __str__(self):
            return f"""
            Corte de MDF "{self.name}" - {self.role} ({self.material})
            Dimensões (mm) {self.width}mm x {self.height}mm Espessura {self.thickness}mm
            Fitas: {self.edge_tapes}
            """


    # Cria o arquivo de saída no diretório "~/Desktop/CutList.csv"
    user_folder = os.path.expanduser("~")
    # make a filename
    filename = os.path.join(user_folder, output_file)
    # confirm path exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # open the file to write to
    file = open(filename, "w")
    # Escreve o cabeçalho do arquivo
    file.write(
        "Quantidade;Comprimento;Largura;Função;Fita C1;Fita C2;Fita L1;Fita L2;Material;Complemento\n"
    )
    # iterate through the selected objects
    for sel in selection:
        if re.search(r"\.\d{3}$", sel.name):
            continue
        if sel.name not in blacklist:
            quantity = 1
            # captura o nome e as dimensões da peça selecionada
            wooden_piece = WoodenPiece(
                name=sel.name,
                dimensions=[
                    int(sel.dimensions.x),
                    int(sel.dimensions.y),
                    int(sel.dimensions.z),
                ],
                material_names=[m.name for m in sel.material_slots],
                role=sel["role"] if "role" in sel else None,
            )
            # Verifica se temos outra peça com o mesmo nome e *.001 para adicionar na quantidade
            for s in selection:
                if re.search(sel.name + r"\.\d{3}$", s.name):
                    blacklist.append(s.name)
                    quantity += 1
            # O comprimento deve ser sempre o maior tamanho, para que a idea ddas fitas funcionem
            width = max(wooden_piece.width, wooden_piece.height)
            height = min(wooden_piece.width, wooden_piece.height)
            # Adiciona a linha ao csv
            file.write(
                f"{quantity};{width};{height};{wooden_piece.role or ''};{wooden_piece.edge_tapes.c1 or ''};{wooden_piece.edge_tapes.c2 or ''};{wooden_piece.edge_tapes.l1 or ''};{wooden_piece.edge_tapes.l2 or ''};{wooden_piece.material};{wooden_piece.name}\n"
            )

    file.close()

def create_example_piece(context):
    # Função que cria um nicho com gaveta suspensa
    bpy.ops.object.select_all(action='DESELECT')
    
    # Creating the niche (a box)
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
    niche = bpy.context.active_object
    niche.scale = (1, 0.5, 1)
    niche.name = "Niche"
    
    # Creating the suspended drawer (a smaller cube)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.5))
    drawer = bpy.context.active_object
    drawer.scale = (0.8, 0.4, 0.2)
    drawer.name = "Suspended Drawer"
    
    print("Example piece created: Niche with suspended drawer")