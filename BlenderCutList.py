import bpy, os, re

# Captura apenas a seleção de objetos no Blender
selection = bpy.context.selected_objects

# Arquivo de saída (edite aqui se necessário)
output_file = 'Desktop/CutList.csv'

# Lista de objetos que não serão analisados (duplicatas)
blacklist = []

# Classe para organizar a fitagem de borda de uma peça
class EdgeTapes:
    def __init__(self, material_names):
        def get_tape_material(tape_identifier: str):
            l = [m for m in material_names if tape_identifier in m]
            return l[0].replace(tape_identifier, '').strip() if len(l) > 0 else None

        # Verifica se existem materiais com identificadores de fitas
        self.c1 = get_tape_material('C1')
        self.c2 = get_tape_material('C2')
        self.l1 = get_tape_material('L1')
        self.l2 = get_tape_material('L2')

    def __str__(self):
        str = ''
        if self.c1:
            str += f'C1: {self.c1} '
        if self.c2:
            str += f'C2: {self.c2} '
        if self.l1:
            str += f'L1: {self.l1} '
        if self.l2:
            str += f'L2: {self.l2} '
        return str

# Classe para organizar as características de um corte do material
class WoodenPiece:
    def __init__(self, dimensions: list, material_names: list, name: str = None, role: str = None):
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
                return f'{m} {self.thickness}mm'
        return None

    def __str__(self):
        return f'''
        Corte de MDF "{self.name}" - {self.role} ({self.material})
        Dimensões (mm) {self.width}mm x {self.height}mm Espessura {self.thickness}mm
        Fitas: {self.edge_tapes}
        '''

# Caminho do arquivo de saída
user_folder = os.path.expanduser('~')
filename = os.path.join(user_folder, output_file)
os.makedirs(os.path.dirname(filename), exist_ok=True)

# Abre o arquivo para escrita
with open(filename, "w") as file:
    # Escreve o cabeçalho
    file.write("Quantidade;Comprimento;Largura;Função;Fita C1;Fita C2;Fita L1;Fita L2;Material;Role\n")
    
    # Itera sobre os objetos selecionados
    for sel in selection:
        if re.search(r"\.\d{3}$", sel.name):
            continue
        if sel.name not in blacklist:
            quantity = 1
            # Captura a propriedade "role" do objeto, se existir
            role = sel.get('role', None)
            # Cria uma instância de WoodenPiece com as dimensões e materiais
            wooden_piece = WoodenPiece(
                name=sel.name, 
                dimensions=[int(sel.dimensions.x), int(sel.dimensions.y), int(sel.dimensions.z)], 
                material_names=[m.name for m in sel.material_slots], 
                role=role
            )
            
            # Verifica duplicatas com o mesmo nome (ex.: *.001) para ajustar a quantidade
            for s in selection:
                if re.search(sel.name + r"\.\d{3}$", s.name):
                    blacklist.append(s.name)
                    quantity += 1

            # O comprimento deve ser sempre o maior tamanho
            width = max(wooden_piece.width, wooden_piece.height)
            height = min(wooden_piece.width, wooden_piece.height)
            
            # Adiciona uma linha ao CSV
            file.write(f"{quantity};{width};{height};{wooden_piece.name};"
                       f"{wooden_piece.edge_tapes.c1 or ''};{wooden_piece.edge_tapes.c2 or ''};"
                       f"{wooden_piece.edge_tapes.l1 or ''};{wooden_piece.edge_tapes.l2 or ''};"
                       f"{wooden_piece.material};{wooden_piece.role or ''}\n")