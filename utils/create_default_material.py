import bpy

def create_default_materials():
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