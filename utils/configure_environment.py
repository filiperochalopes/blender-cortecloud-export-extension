"""
Configurações de ambiente para uma melhor edição e visualização dos móveis
"""

# Importando a API do blender
import bpy

# Configurações de ambiente para melhor uso em móveis e precisão
def configure_environment():
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
            print(f"Objeto {obj.name} ({obj.type}) removido.")
            
    # Atualizando para correção de medidas em script em relação ao viewport
    bpy.context.view_layer.update()