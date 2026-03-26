import bpy
import json
import math
from mathutils import Vector


def round3(value):
    return round(float(value), 3)


def get_scene_mm_factor():
    """
    Retorna o fator para converter unidades do Blender para milímetros.
    """
    settings = bpy.context.scene.unit_settings
    scale_length = settings.scale_length if settings.scale_length else 1.0

    if settings.system == 'METRIC':
        return 1000.0 * scale_length

    return 1000.0 * scale_length


def vec_to_dict_mm(vec, factor):
    return {
        "x": round3(vec.x * factor),
        "y": round3(vec.y * factor),
        "z": round3(vec.z * factor),
    }


def vec_to_dict(vec):
    return {
        "x": round3(vec.x),
        "y": round3(vec.y),
        "z": round3(vec.z),
    }


def get_world_bbox_dimensions_mm(obj, factor):
    corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    min_x = min(v.x for v in corners)
    max_x = max(v.x for v in corners)
    min_y = min(v.y for v in corners)
    max_y = max(v.y for v in corners)
    min_z = min(v.z for v in corners)
    max_z = max(v.z for v in corners)

    return {
        "x": round3((max_x - min_x) * factor),
        "y": round3((max_y - min_y) * factor),
        "z": round3((max_z - min_z) * factor),
    }


def get_cut_dimensions_mm(obj, factor):
    dims = list(get_world_bbox_dimensions_mm(obj, factor).values())
    dims_sorted = sorted(dims, reverse=True)

    return {
        "comprimento": round3(dims_sorted[0]),
        "largura": round3(dims_sorted[1]),
        "espessura": round3(dims_sorted[2]),
    }


def polygon_center_world(obj, poly):
    return obj.matrix_world @ poly.center


def polygon_normal_world(obj, poly):
    normal_matrix = obj.matrix_world.to_3x3().inverted().transposed()
    n = normal_matrix @ poly.normal
    return n.normalized()


def polygon_vertices_local_mm(mesh, poly, factor):
    return [
        vec_to_dict_mm(mesh.vertices[v_idx].co, factor)
        for v_idx in poly.vertices
    ]


def polygon_vertices_world_mm(obj, mesh, poly, factor):
    return [
        vec_to_dict_mm(obj.matrix_world @ mesh.vertices[v_idx].co, factor)
        for v_idx in poly.vertices
    ]


def get_face_signature(obj, poly):
    """
    Gera uma assinatura geométrica simples da face para futura reconstrução:
    eixo dominante da normal + sinal + centro arredondado em local.
    """
    n = poly.normal.normalized()
    axis_values = {
        "x": abs(n.x),
        "y": abs(n.y),
        "z": abs(n.z),
    }
    dominant_axis = max(axis_values, key=axis_values.get)

    if dominant_axis == "x":
        sign = "+" if n.x >= 0 else "-"
    elif dominant_axis == "y":
        sign = "+" if n.y >= 0 else "-"
    else:
        sign = "+" if n.z >= 0 else "-"

    c = poly.center
    return f"{dominant_axis}{sign}@{round3(c.x)},{round3(c.y)},{round3(c.z)}"


def get_material_assignments(obj, factor):
    """
    Retorna:
    - slots de material
    - uso real por faces
    - slots sem uso
    - faces detalhadas com geometria
    """
    result = {
        "slots": [],
        "face_usage": [],
        "unused_slots": [],
        "faces": [],
    }

    if obj.type != 'MESH' or not obj.data:
        return result

    mesh = obj.data
    poly_counts = {}
    faces_by_slot = {}

    for poly in mesh.polygons:
        idx = poly.material_index
        poly_counts[idx] = poly_counts.get(idx, 0) + 1
        faces_by_slot.setdefault(idx, []).append(poly.index)

        material_name = None
        if 0 <= idx < len(obj.material_slots):
            slot = obj.material_slots[idx]
            material_name = slot.material.name if slot.material else None

        face_info = {
            "polygon_index": poly.index,
            "material_index": idx,
            "material": material_name,
            "loop_total": poly.loop_total,
            "vertex_count": len(poly.vertices),
            "area_mm2": round3(poly.area * (factor ** 2)),
            "center_local_mm": vec_to_dict_mm(poly.center, factor),
            "center_world_mm": vec_to_dict_mm(polygon_center_world(obj, poly), factor),
            "normal_local": vec_to_dict(poly.normal.normalized()),
            "normal_world": vec_to_dict(polygon_normal_world(obj, poly)),
            "face_signature": get_face_signature(obj, poly),
            "vertices_local_mm": polygon_vertices_local_mm(mesh, poly, factor),
            "vertices_world_mm": polygon_vertices_world_mm(obj, mesh, poly, factor),
        }
        result["faces"].append(face_info)

    for idx, slot in enumerate(obj.material_slots):
        material_name = slot.material.name if slot.material else None
        face_count = poly_counts.get(idx, 0)
        polygon_indices = faces_by_slot.get(idx, [])

        slot_info = {
            "slot_index": idx,
            "material": material_name,
            "face_count": face_count,
            "polygon_indices": polygon_indices,
            "used": face_count > 0,
        }

        result["slots"].append(slot_info)

        if face_count > 0:
            result["face_usage"].append(slot_info)
        else:
            result["unused_slots"].append(slot_info)

    return result


def get_custom_props(obj):
    return {
        k: obj[k]
        for k in obj.keys()
        if k != "_RNA_UI"
    }


def obj_to_dict(obj, mm_factor):
    return {
        "name": obj.name,
        "type": obj.type,
        "is_mesh": obj.type == 'MESH',
        "dimensions_mm": get_world_bbox_dimensions_mm(obj, mm_factor),
        "cut_dimensions_mm": get_cut_dimensions_mm(obj, mm_factor),
        "location_mm": vec_to_dict_mm(obj.matrix_world.translation, mm_factor),
        "rotation_deg": {
            "x": round3(math.degrees(obj.rotation_euler.x)),
            "y": round3(math.degrees(obj.rotation_euler.y)),
            "z": round3(math.degrees(obj.rotation_euler.z)),
        },
        "scale": {
            "x": round3(obj.scale.x),
            "y": round3(obj.scale.y),
            "z": round3(obj.scale.z),
        },
        "materials": [slot.material.name for slot in obj.material_slots if slot.material],
        "material_assignments": get_material_assignments(obj, mm_factor),
        "custom_props": get_custom_props(obj),
    }


selected = list(bpy.context.selected_objects)
mm_factor = get_scene_mm_factor()

data = {
    "meta": {
        "selected_count": len(selected),
        "scene_unit_system": bpy.context.scene.unit_settings.system,
        "scene_scale_length": bpy.context.scene.unit_settings.scale_length,
        "mm_factor": round3(mm_factor),
        "all_selected_are_mesh": all(obj.type == 'MESH' for obj in selected),
    },
    "objects": [obj_to_dict(obj, mm_factor) for obj in selected],
}

print("================ Selected data export (start) =================")
print(json.dumps(data, indent=2, ensure_ascii=False))
print("================ Selected data export (end) =================")