"""
Configurações de ambiente para uma melhor edição e visualização dos móveis
"""

# Importando a API do blender
import bpy

# Configurações de ambiente para melhor uso em móveis e precisão
unit_settings = bpy.context.scene.unit_settings
unit_settings.system = 'METRIC'
unit_settings.scale_length = 0.001
unit_settings.length_unit = 'MILLIMETERS'
unit_settings.system_rotation = 'DEGREES'
# Cada cena é composta de várias áreas/janelas
areas = [a for a in bpy.context.screen.areas if a.type == 'VIEW_3D']
spaces = [s for s in areas if s.type == 'VIEW_3D']
workspace = None
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

# Removendo todas as luzes e câmeras do ambiente
for obj in bpy.context.scene.objects:
    if obj.type == 'LIGHT' or obj.type == 'CAMERA':
        bpy.data.objects.remove(obj, do_unlink=True)
        print(f"Objeto {obj.name} ({obj.type}) removido.")

# Atualizando para correção de medidas em script em relação ao viewport
bpy.context.view_layer.update()