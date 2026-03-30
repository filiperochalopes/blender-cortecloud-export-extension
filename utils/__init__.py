import bpy, bmesh, json, os, re  # noqa: E401

ADDON_ROOT = os.path.dirname(os.path.dirname(__file__))
DRAWER_PARTS_FILE = os.path.join(ADDON_ROOT, "assets", "drawer_parts.json")
WHITE_MDF_MATERIAL = "White MDF"
EDGE_BANDING_MATERIAL = "Edge Banding"
LEGACY_EDGE_BANDING_MATERIAL = "Edge Banding (Com fita)"
NO_EDGE_BANDING_MATERIAL = "No Edge Banding"
AXIS_ORDER = ("x", "y", "z")
DEFAULT_MATERIAL_COLORS = {
    WHITE_MDF_MATERIAL: (0.905, 0.905, 0.905, 1),
    EDGE_BANDING_MATERIAL: (1.0, 0.862, 0.0, 1),
    NO_EDGE_BANDING_MATERIAL: (0.866, 0, 0.905, 1),
}
IDENTIFIED_THICKNESSES = (6, 9, 15, 18)


def normalize_material_name(material_name):
    return material_name.strip() if material_name else None


def sanitize_edge_banding_name(material_name):
    material_name = normalize_material_name(material_name)
    if not material_name:
        return EDGE_BANDING_MATERIAL

    cleaned_name = re.sub(r"\s*\(Com\s+fita\)", "", material_name, flags=re.IGNORECASE)
    cleaned_name = re.sub(r"\s{2,}", " ", cleaned_name).strip(" -")
    return cleaned_name or EDGE_BANDING_MATERIAL


def get_material_aliases(material_name):
    aliases = [material_name]
    if material_name == EDGE_BANDING_MATERIAL:
        aliases.append(LEGACY_EDGE_BANDING_MATERIAL)
    return aliases


def find_material(material_name):
    for alias in get_material_aliases(material_name):
        material = bpy.data.materials.get(alias)
        if material is None:
            continue

        if alias != material_name and bpy.data.materials.get(material_name) is None:
            material.name = material_name

        return bpy.data.materials.get(material_name) or material

    return None


def is_edge_banding_material(material_name):
    material_name = normalize_material_name(material_name)
    if not material_name:
        return False

    return (
        material_name == EDGE_BANDING_MATERIAL
        or material_name == LEGACY_EDGE_BANDING_MATERIAL
        or material_name.startswith("Edge Banding")
        or bool(re.search(r"\b(C1|C2|L1|L2)\b", material_name))
    )


def is_no_edge_banding_material(material_name):
    material_name = normalize_material_name(material_name)
    if not material_name:
        return False

    return (
        material_name == NO_EDGE_BANDING_MATERIAL
        or material_name.startswith("No Edge Banding")
        or "Sem Fita" in material_name
    )


def is_main_board_material(material_name):
    material_name = normalize_material_name(material_name)
    return bool(material_name) and not is_edge_banding_material(material_name) and not is_no_edge_banding_material(material_name)


def get_exported_edge_banding_name(material_name):
    material_name = normalize_material_name(material_name)
    if not material_name:
        return EDGE_BANDING_MATERIAL

    cleaned_name = re.sub(r"\b(C1|C2|L1|L2)\b", "", material_name).strip(" -")
    if is_edge_banding_material(material_name):
        return sanitize_edge_banding_name(cleaned_name)

    return cleaned_name or EDGE_BANDING_MATERIAL


def get_material_name_from_slot(slot):
    if slot is None or slot.material is None:
        return None

    return normalize_material_name(slot.material.name)


def get_material_names_from_object(obj):
    material_names = []

    for slot in obj.material_slots:
        material_name = get_material_name_from_slot(slot)
        if material_name:
            material_names.append(material_name)

    return material_names


def get_object_axis_dimensions(obj):
    return {
        "x": abs(float(obj.dimensions.x)),
        "y": abs(float(obj.dimensions.y)),
        "z": abs(float(obj.dimensions.z)),
    }


def get_cut_axes_from_dimensions(axis_dimensions):
    thickness_axis = min(
        AXIS_ORDER,
        key=lambda axis: (axis_dimensions[axis], AXIS_ORDER.index(axis)),
    )
    planar_axes = [axis for axis in AXIS_ORDER if axis != thickness_axis]
    planar_axes.sort(
        key=lambda axis: (-axis_dimensions[axis], AXIS_ORDER.index(axis)),
    )

    comprimento_axis = planar_axes[0]
    largura_axis = planar_axes[1]

    return {
        "thickness_axis": thickness_axis,
        "comprimento_axis": comprimento_axis,
        "largura_axis": largura_axis,
        "comprimento": axis_dimensions[comprimento_axis],
        "largura": axis_dimensions[largura_axis],
        "espessura": axis_dimensions[thickness_axis],
    }


def get_dominant_axis_and_sign_from_polygon(polygon):
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

    return dominant_axis, sign


def get_polygon_material_name(obj, polygon):
    if polygon.material_index < 0 or polygon.material_index >= len(obj.material_slots):
        return None

    return get_material_name_from_slot(obj.material_slots[polygon.material_index])


def get_main_material_label(material_names, thickness):
    rounded_thickness = round(thickness)

    for material_name in material_names:
        if is_main_board_material(material_name):
            return f"{material_name} {rounded_thickness}mm"

    return None


def get_object_main_material_name(obj):
    material_names = get_material_names_from_object(obj)

    for material_name in material_names:
        if "MDF" in material_name.upper():
            return material_name

    for material_name in material_names:
        if is_main_board_material(material_name):
            return material_name

    return "Not identified"


def group_edge_faces_for_export(obj, cut_axes):
    grouped_sides = {}

    for polygon in obj.data.polygons:
        axis, sign = get_dominant_axis_and_sign_from_polygon(polygon)
        if axis == cut_axes["thickness_axis"]:
            continue

        side_signature = f"{axis}{sign}"
        side_info = grouped_sides.setdefault(
            side_signature,
            {"axis": axis, "sign": sign, "materials": []},
        )

        material_name = get_polygon_material_name(obj, polygon)
        if material_name:
            side_info["materials"].append(material_name)

    edge_groups = {"C": [], "L": []}

    for side_info in grouped_sides.values():
        edge_banding_name = None

        for material_name in side_info["materials"]:
            if is_edge_banding_material(material_name):
                edge_banding_name = get_exported_edge_banding_name(material_name)
                break

        side_info["edge_banding"] = edge_banding_name

        if side_info["axis"] == cut_axes["largura_axis"]:
            edge_groups["C"].append(side_info)
        elif side_info["axis"] == cut_axes["comprimento_axis"]:
            edge_groups["L"].append(side_info)

    for group_name in edge_groups:
        edge_groups[group_name].sort(key=lambda side: 0 if side["sign"] == "-" else 1)

    return edge_groups


def get_edge_tape_columns(edge_sides):
    edge_banding_materials = [side["edge_banding"] for side in edge_sides if side["edge_banding"]]

    if not edge_banding_materials:
        return "", ""

    if len(edge_banding_materials) == 1:
        return edge_banding_materials[0], ""

    return edge_banding_materials[0], edge_banding_materials[1]


def get_edge_tapes_from_object(obj, cut_axes):
    edge_groups = group_edge_faces_for_export(obj, cut_axes)
    c1, c2 = get_edge_tape_columns(edge_groups["C"])
    l1, l2 = get_edge_tape_columns(edge_groups["L"])

    return {
        "c1": c1,
        "c2": c2,
        "l1": l1,
        "l2": l2,
    }


def get_object_thickness_label(obj):
    cut_axes = get_cut_axes_from_dimensions(get_object_axis_dimensions(obj))
    thickness = round(cut_axes["espessura"])

    if thickness in IDENTIFIED_THICKNESSES:
        return f"{thickness}mm"

    return "Not identified"


def get_object_edge_banding_labels(obj):
    cut_axes = get_cut_axes_from_dimensions(get_object_axis_dimensions(obj))
    edge_tapes = get_edge_tapes_from_object(obj, cut_axes)
    edge_labels = []

    for label in ("L1", "L2", "C1", "C2"):
        if edge_tapes[label.lower()]:
            edge_labels.append(label)

    return edge_labels


def get_object_edge_banding_label(obj):
    edge_labels = get_object_edge_banding_labels(obj)
    return ", ".join(edge_labels) if edge_labels else "None"


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


def get_window_and_screen(context):
    window = getattr(context, "window", None)
    screen = getattr(context, "screen", None)

    if screen is None and window is not None:
        screen = window.screen

    if window is None:
        window = getattr(bpy.context, "window", None)

    if screen is None and window is not None:
        screen = window.screen

    if screen is None:
        screen = getattr(bpy.context, "screen", None)

    if window is None and screen is not None:
        window_manager = getattr(bpy.context, "window_manager", None)
        if window_manager is not None:
            for candidate_window in window_manager.windows:
                if candidate_window.screen == screen:
                    window = candidate_window
                    break

    return window, screen


def get_area_window_region(area):
    return next((region for region in area.regions if region.type == 'WINDOW'), None)


def get_largest_view_3d_area(screen):
    view_3d_areas = [area for area in screen.areas if area.type == 'VIEW_3D']
    if not view_3d_areas:
        return None

    return max(view_3d_areas, key=lambda area: area.width * area.height)


def configure_outliner_area(context, window, screen, area):
    region = get_area_window_region(area)
    override_args = {"window": window, "screen": screen, "area": area}
    if region is not None:
        override_args["region"] = region

    try:
        with context.temp_override(**override_args):
            bpy.ops.wm.context_set_enum(data_path="area.type", value='OUTLINER')
    except RuntimeError:
        area.type = 'OUTLINER'
    else:
        area.type = 'OUTLINER'

    try:
        area.ui_type = 'OUTLINER'
    except TypeError:
        pass

    for space in area.spaces:
        if space.type == 'OUTLINER':
            space.display_mode = 'VIEW_LAYER'
            break


def ensure_outliner_area(context, window, screen):
    close_outliner_areas(context)

    source_area = get_largest_view_3d_area(screen)
    if source_area is None:
        return None

    region = get_area_window_region(source_area)
    override_args = {"window": window, "screen": screen, "area": source_area}
    if region is not None:
        override_args["region"] = region

    try:
        with context.temp_override(**override_args):
            result = bpy.ops.screen.area_split(direction='VERTICAL', factor=0.2)
    except RuntimeError:
        return None

    if 'FINISHED' not in result:
        return None

    all_areas = [area for area in screen.areas]
    if not all_areas:
        return None

    outliner_area = all_areas[-1]
    configure_outliner_area(context, window, screen, outliner_area)
    return outliner_area


def close_outliner_areas(context, keep_areas=None):
    window, screen = get_window_and_screen(context)
    if window is None or screen is None:
        return

    keep_area_pointers = {area.as_pointer() for area in (keep_areas or [])}
    outliner_areas = [
        area for area in screen.areas
        if area.type == 'OUTLINER' and area.as_pointer() not in keep_area_pointers
    ]
    outliner_areas.sort(key=lambda area: area.x, reverse=True)

    for area in outliner_areas:
        if len(screen.areas) <= 1:
            break

        region = get_area_window_region(area)

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

    window, screen = get_window_and_screen(context)
    if window is not None and screen is not None:
        ensure_outliner_area(context, window, screen)

    areas = [area for area in screen.areas if area.type == 'VIEW_3D'] if screen is not None else []

    # Configurando área de seleção de objetos
    for area in areas:
        for s in area.spaces:
            if s.type == 'VIEW_3D':
                s.shading.type = 'SOLID'
                s.shading.show_xray = True
                s.overlay.grid_scale = 0.001
                s.clip_start = 0.1
                s.clip_end = 10000

    # Alterando o clipping point da camera ativa, caso exista uma
    if context.scene.camera:
        context.scene.camera.data.clip_start = 0.1
        context.scene.camera.data.clip_end = 10000

    # Removendo todas as luzes e câmeras do ambiente
    for obj in list(context.scene.objects):
        if obj.type == 'LIGHT' or obj.type == 'CAMERA':
            bpy.data.objects.remove(obj, do_unlink=True)
            
    # Atualizando para correção de medidas em script em relação ao viewport
    view_layer = getattr(context, "view_layer", None) or getattr(bpy.context, "view_layer", None)
    if view_layer is not None:
        view_layer.update()


def create_default_materials(context):
    for material_name, color in DEFAULT_MATERIAL_COLORS.items():
        material = find_material(material_name)

        if material is None:
            material = bpy.data.materials.new(name=material_name)
            print(f"Material {material_name} criado.")
        else:
            print(f"Material {material_name} já existe.")

        material.diffuse_color = color

    # Atualizando para correção de medidas em script em relação ao viewport
    context.view_layer.update()



def export_to_csv(filepath):
    # Adiciona ".csv" ao nome do arquivo se o usuário não adicionar
    if not filepath.endswith(".csv"):
        filepath += ".csv"

    # Captura apenas a seleção, gosto de utilizar coleções de madeira e outras de outros materiais, dessa forma fica fácil selecionar apenas os itens de madeira
    selection = bpy.context.selected_objects
    # Para cada objeto selecionado, aplica a transformação de escala e rotação
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    bpy.context.view_layer.update()

    # Arquivo de saída (edite aqui)
    output_file = filepath
    # lista de nome de objetos que não deverão ser analisados, pois são duplicatas de outros objetos. São esses os de final *.001, *.002 ...
    blacklist = []


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
        if sel.type != 'MESH':
            continue

        if re.search(r"\.\d{3}$", sel.name):
            continue
        if sel.name not in blacklist:
            quantity = 1
            material_names = get_material_names_from_object(sel)
            cut_axes = get_cut_axes_from_dimensions(get_object_axis_dimensions(sel))
            edge_tapes = get_edge_tapes_from_object(sel, cut_axes)
            material = get_main_material_label(material_names, cut_axes["espessura"])

            # Verifica se temos outra peça com o mesmo nome e *.001 para adicionar na quantidade
            for s in selection:
                if re.search(sel.name + r"\.\d{3}$", s.name):
                    blacklist.append(s.name)
                    quantity += 1

            # Adiciona a linha ao csv
            file.write(
                f"{quantity};{round(cut_axes['comprimento'])};{round(cut_axes['largura'])};{sel['role'] if 'role' in sel else ''};{edge_tapes['c1']};{edge_tapes['c2']};{edge_tapes['l1']};{edge_tapes['l2']};{material};{sel.name}\n"
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
    material = find_material(name)
    if material is None:
        material = bpy.data.materials.new(name=name)
        if name in DEFAULT_MATERIAL_COLORS:
            material.diffuse_color = DEFAULT_MATERIAL_COLORS[name]
    return material


def ensure_collection(name):
    collection = bpy.data.collections.get(name)
    if collection is None:
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
    return collection


def get_face_signature_from_polygon(polygon):
    dominant_axis, sign = get_dominant_axis_and_sign_from_polygon(polygon)
    return f"{dominant_axis}{sign}"


def build_material_slot_map(obj, material_names):
    obj.data.materials.clear()
    material_slot_map = {}

    for material_name in material_names:
        if material_name in material_slot_map:
            continue

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
