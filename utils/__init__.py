import bpy, bmesh, json, os, re  # noqa: E401

ADDON_ROOT = os.path.dirname(os.path.dirname(__file__))
DRAWER_PARTS_FILE = os.path.join(ADDON_ROOT, "assets", "drawer_parts.json")


def load_drawer_parts():
    with open(DRAWER_PARTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def _ranges_overlap(start_a, size_a, start_b, size_b):
    end_a = start_a + size_a
    end_b = start_b + size_b
    return min(end_a, end_b) > max(start_a, start_b)


def _get_area_center(area):
    return (
        area.x + int(area.width / 2),
        area.y + int(area.height / 2),
    )


def _find_area_to_join(screen, source_area):
    best_area = None
    best_score = -1

    for area in screen.areas:
        if area == source_area:
            continue

        shares_vertical_border = (
            (source_area.x + source_area.width == area.x or area.x + area.width == source_area.x)
            and _ranges_overlap(source_area.y, source_area.height, area.y, area.height)
        )
        shares_horizontal_border = (
            (source_area.y + source_area.height == area.y or area.y + area.height == source_area.y)
            and _ranges_overlap(source_area.x, source_area.width, area.x, area.width)
        )

        if not shares_vertical_border and not shares_horizontal_border:
            continue

        score = 2 if area.type == 'VIEW_3D' else 1
        if score > best_score:
            best_area = area
            best_score = score

    return best_area


def close_outliner_areas(context):
    screen = context.screen
    window = context.window
    outliner_areas = [area for area in screen.areas if area.type == 'OUTLINER']

    for area in outliner_areas:
        if len(screen.areas) <= 1:
            break

        region = next((region for region in area.regions if region.type == 'WINDOW'), None)

        try:
            override_args = {"window": window, "screen": screen, "area": area}
            if region:
                override_args["region"] = region

            with context.temp_override(**override_args):
                result = bpy.ops.screen.area_close()

            if 'FINISHED' in result:
                continue
        except RuntimeError:
            pass

        target_area = _find_area_to_join(screen, area)
        if not target_area:
            continue

        with context.temp_override(window=window, screen=screen, area=area):
            bpy.ops.screen.area_join(
                source_xy=_get_area_center(area),
                target_xy=_get_area_center(target_area),
            )

# Configurações de ambiente para melhor uso em móveis e precisão
def configure_environment(context):
    unit_settings = context.scene.unit_settings
    unit_settings.system = 'METRIC'
    unit_settings.scale_length = 0.001
    unit_settings.length_unit = 'MILLIMETERS'
    unit_settings.system_rotation = 'DEGREES'
    # Ativando função de snap para vértice
    tool_settings = context.scene.tool_settings
    tool_settings.use_snap = True
    tool_settings.snap_elements_base = {'VERTEX'}
    # Fechando Outliners já abertos no layout
    close_outliner_areas(context)

    # Cada cena é composta de várias áreas/janelas
    areas = [a for a in context.screen.areas if a.type == 'VIEW_3D']

    # Configurando área de seleção de objetos
    for area in areas:
        for s in area.spaces:
            if s.type == 'VIEW_3D':
                s.shading.type = 'SOLID'
                s.shading.show_xray = True
                s.overlay.grid_scale = 0.001
                s.clip_start = 0.1
                s.clip_end = 1000000

    # Alterando o clipping point da camera ativa, caso exista uma
    if context.scene.camera:
        context.scene.camera.data.clip_end = 1000000

    # Removendo todas as luzes e câmeras do ambiente
    for obj in context.scene.objects:
        if obj.type == 'LIGHT' or obj.type == 'CAMERA':
            bpy.data.objects.remove(obj, do_unlink=True)
            
    # Atualizando para correção de medidas em script em relação ao viewport
    context.view_layer.update()


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
    create_material('MDF White - Branco', (0.905, 0.905, 0.905, 1))  # #E7E7E7
    create_material('L1 White - Branco', (0, 0.905, 0.890, 1))       # #00E7E3
    create_material('L2 White - Branco', (0, 0.905, 0.890, 1))       # #00E7E3
    create_material('C1 White - Branco', (0, 0.905, 0.890, 1))       # #00E7E3
    create_material('C2 White - Branco', (0, 0.905, 0.890, 1))       # #00E7E3
    create_material('No Edge Ribbons - Sem Fita', (0.866, 0, 0.905, 1))        # #DD00E7

    # Atualizando para correção de medidas em script em relação ao viewport
    bpy.context.view_layer.update()



def export_to_csv(filepath):
    # Adiciona ".csv" ao nome do arquivo se o usuário não adicionar
    if not filepath.endswith(".csv"):
        filepath += ".csv"

    # Captura apenas a seleção, gosto de utilizar coleções de madeira e outras de outros materiais, dessa forma fica fácil selecionar apenas os itens de madeira
    selection = bpy.context.selected_objects
    # Para cada objeto selecionado, aplica a transformação de escala e rotação
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

    # Arquivo de saída (edite aqui)
    output_file = filepath
    # lista de nome de objetos que não deverão ser analisados, pois são duplicatas de outros objetos. São esses os de final *.001, *.002 ...
    blacklist = []


    # classe para organizar a fitagem de borda de uma peça
    class EdgeTapes:
        def __init__(self, material_names):
            def get_tape_material(tape_identifier: str):
                matching_materials = [m for m in material_names if tape_identifier in m]
                return matching_materials[0].replace(tape_identifier, "").strip() if len(matching_materials) > 0 else None

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
                    round(sel.dimensions.x),
                    round(sel.dimensions.y),
                    round(sel.dimensions.z),
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

def get_scene_scale_length():
    unit_settings = bpy.context.scene.unit_settings
    return unit_settings.scale_length if unit_settings.scale_length else 1.0


def mm_to_scene_units(mm):
    return mm / (1000.0 * get_scene_scale_length())


def vec_mm_to_scene(coords):
    return (
        mm_to_scene_units(coords["x"]),
        mm_to_scene_units(coords["y"]),
        mm_to_scene_units(coords["z"]),
    )


def ensure_material(name):
    material = bpy.data.materials.get(name)
    if material is None:
        material = bpy.data.materials.new(name=name)
    return material


def ensure_collection(name):
    collection = bpy.data.collections.get(name)
    if collection is None:
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
    return collection


def get_face_signature_from_polygon(polygon):
    normal = polygon.normal.normalized()

    axis_values = {
        "x": abs(normal.x),
        "y": abs(normal.y),
        "z": abs(normal.z),
    }
    dominant_axis = max(axis_values, key=axis_values.get)

    if dominant_axis == "x":
        sign = "+" if normal.x >= 0 else "-"
    elif dominant_axis == "y":
        sign = "+" if normal.y >= 0 else "-"
    else:
        sign = "+" if normal.z >= 0 else "-"

    return f"{dominant_axis}{sign}"


def build_material_slot_map(obj, material_names):
    obj.data.materials.clear()
    material_slot_map = {}

    for material_name in material_names:
        obj.data.materials.append(ensure_material(material_name))
        material_slot_map[material_name] = len(obj.data.materials) - 1

    return material_slot_map


def assign_drawer_materials(obj, drawer_piece):
    material_slot_map = build_material_slot_map(obj, drawer_piece["materials"])

    for polygon in obj.data.polygons:
        face_signature = get_face_signature_from_polygon(polygon)
        material_name = drawer_piece["face_materials"].get(face_signature)
        if material_name is None:
            continue
        polygon.material_index = material_slot_map[material_name]

    obj.data.update()


def create_box_mesh_object(name, dimensions_mm, location_scene, collection):
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)

    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=2.0)
    bm.to_mesh(mesh)
    bm.free()

    obj.location = location_scene
    obj.rotation_euler = (0.0, 0.0, 0.0)
    obj.scale = (
        mm_to_scene_units(dimensions_mm["x"]) / 2.0,
        mm_to_scene_units(dimensions_mm["y"]) / 2.0,
        mm_to_scene_units(dimensions_mm["z"]) / 2.0,
    )

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.select_set(False)

    return obj


def compute_group_center_scene(drawer_parts):
    mins = [float("inf"), float("inf"), float("inf")]
    maxs = [float("-inf"), float("-inf"), float("-inf")]

    for drawer_piece in drawer_parts:
        location_scene = vec_mm_to_scene(drawer_piece["location_mm"])
        dimensions_scene = (
            mm_to_scene_units(drawer_piece["dimensions_mm"]["x"]),
            mm_to_scene_units(drawer_piece["dimensions_mm"]["y"]),
            mm_to_scene_units(drawer_piece["dimensions_mm"]["z"]),
        )
        half_dimensions = [value / 2.0 for value in dimensions_scene]

        for index in range(3):
            mins[index] = min(mins[index], location_scene[index] - half_dimensions[index])
            maxs[index] = max(maxs[index], location_scene[index] + half_dimensions[index])

    return tuple((mins[index] + maxs[index]) / 2.0 for index in range(3))


def create_drawer(context):
    drawer_parts = load_drawer_parts()
    collection = ensure_collection("Drawer")
    cursor_location = context.scene.cursor.location.copy()
    group_center = compute_group_center_scene(drawer_parts)
    translation = (
        cursor_location.x - group_center[0],
        cursor_location.y - group_center[1],
        cursor_location.z - group_center[2],
    )

    created_objects = []

    bpy.ops.object.select_all(action='DESELECT')

    for drawer_piece in drawer_parts:
        original_location = vec_mm_to_scene(drawer_piece["location_mm"])
        location_scene = (
            original_location[0] + translation[0],
            original_location[1] + translation[1],
            original_location[2] + translation[2],
        )

        obj = create_box_mesh_object(
            name=drawer_piece["name"],
            dimensions_mm=drawer_piece["dimensions_mm"],
            location_scene=location_scene,
            collection=collection,
        )
        assign_drawer_materials(obj, drawer_piece)
        created_objects.append(obj)

    for obj in created_objects:
        obj.select_set(True)

    if created_objects:
        bpy.context.view_layer.objects.active = created_objects[0]

    print(f"Gaveta criada com {len(created_objects)} peças.")
