bl_info = {
    "name": "CorteCloud Export Utils",
    "blender": (3, 0, 0),
    "category": "Object",
}

import bpy
import os
from bpy.props import StringProperty
from . import utils

# Operator to configure environment
class OBJECT_OT_configure_environment(bpy.types.Operator):
    bl_idname = "object.configure_environment"
    bl_label = "Configure Environment"
    
    def execute(self, context):
        utils.configure_environment(context)
        return {'FINISHED'}

# Operator to create base materials
class OBJECT_OT_create_base_materials(bpy.types.Operator):
    bl_idname = "object.create_base_materials"
    bl_label = "Create Base Materials"
    
    def execute(self, context):
        utils.create_default_materials(context)
        return {'FINISHED'}

# Operator to export CSV
class OBJECT_OT_export_to_csv(bpy.types.Operator):
    bl_idname = "object.export_to_csv"
    bl_label = "Export to CSV"
    
    filepath: StringProperty(subtype="FILE_PATH", default="cortecloud-export-list.csv")  # Nome padrão
    
    def execute(self, context):
        utils.export_to_csv(self.filepath)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# Operator to create example piece
class OBJECT_OT_create_example_piece(bpy.types.Operator):
    bl_idname = "object.create_example_piece"
    bl_label = "Create Example Piece (WIP)"
    
    def execute(self, context):
        utils.create_example_piece(context)
        return {'FINISHED'}

# Panel in the N region to hold the buttons
class OBJECT_PT_cortecloud_panel(bpy.types.Panel):
    bl_label = "CorteCloud Export Utils"
    bl_idname = "OBJECT_PT_cortecloud_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CorteCloud'
    
    def draw(self, context):
        layout = self.layout
        
        # Botão para configurar ambiente
        layout.operator("object.configure_environment", text="Configure Environment")
        
        # Botão para criar materiais base
        layout.operator("object.create_base_materials", text="Create Base Materials")
        
        # Botão para exportar CSV
        layout.operator("object.export_to_csv", text="Export to CSV")
        
        # Botão para criar exemplo de peça
        layout.operator("object.create_example_piece", text="Create Example Piece")

func_options = [
    ('CONTRA_FRENTE_FUNDO_GAVETA', 'Contra Frente / Contra Fundo de Gaveta', ''),
    ('LATERAL_GAVETA', 'Lateral de Gaveta', ''),
    ('PORTA', 'Porta', ''),
    ('LATERAL_DIREITA', 'Lateral Direita', ''),
    ('LATERAL_ESQUERDA', 'Lateral Esquerda', ''),
    ('TAMPO', 'Tampo', ''),
    ('BASE', 'Base', ''),
    ('NONE', '', ''),
]

# Função chamada quando a propriedade é alterada
def update_role_property(self, context):
    self["role"] = next((item[1] for item in func_options if item[0] == self.funcao_enum), "")  # Adiciona a função selecionada à propriedade 'role' do objeto

# Adicionando a propriedade de enumeração aos objetos do tipo Object
def add_custom_enum_property():
    bpy.types.Object.funcao_enum = bpy.props.EnumProperty(
        name="Função", 
        description="Selecione a função da peça", 
        items=func_options,
        default='NONE',  # Definindo 'BASE' como o valor padrão
        update=update_role_property  # Chama a função ao atualizar a enum
    )

# Criando o painel para exibir a propriedade no painel lateral (tecla N)
class VIEW3D_PT_custom_panel(bpy.types.Panel):
    bl_label = "CorteCloud Export Utils"
    bl_idname = "VIEW3D_PT_custom_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'

    def draw(self, context):
        layout = self.layout
        obj = context.object

        # Exibe a propriedade enum se o objeto estiver selecionado
        if obj is not None:
            layout.prop(obj, "funcao_enum")
            # Mostra também o valor atual da propriedade 'role' (opcional)
            layout.label(text=f"Role: {obj.get('role', 'None')}")

            # Adiciona dois botões para ajustar o tamanho Z
            layout.operator("object.set_z_15", text="15mm")
            layout.operator("object.set_z_18", text="18mm")

# Define as funções dos botões
class OBJECT_OT_set_z_15(bpy.types.Operator):
    bl_idname = "object.set_z_15"
    bl_label = "Set Z to 15mm"
    
    def execute(self, context):
        obj = context.object
        if obj is not None:
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
            obj.dimensions.z = 15  # Define a altura para 15mm (escala em metros)
            bpy.ops.object.transform_apply(scale=True)
        return {'FINISHED'}

class OBJECT_OT_set_z_18(bpy.types.Operator):
    bl_idname = "object.set_z_18"
    bl_label = "Set Z to 18mm"
    
    def execute(self, context):
        obj = context.object
        if obj is not None:
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
            obj.dimensions.z = 18  # Define a altura para 18mm (escala em metros)
            bpy.ops.object.transform_apply(scale=True)
        return {'FINISHED'}
    
# Registro das classes do plugin
def register():
    bpy.utils.register_class(OBJECT_OT_configure_environment)
    bpy.utils.register_class(OBJECT_OT_create_base_materials)
    bpy.utils.register_class(OBJECT_OT_export_to_csv)
    bpy.utils.register_class(OBJECT_OT_create_example_piece)
    bpy.utils.register_class(OBJECT_PT_cortecloud_panel)
    bpy.utils.register_class(VIEW3D_PT_custom_panel)
    bpy.utils.register_class(OBJECT_OT_set_z_15)
    bpy.utils.register_class(OBJECT_OT_set_z_18)
    add_custom_enum_property()

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_configure_environment)
    bpy.utils.unregister_class(OBJECT_OT_create_base_materials)
    bpy.utils.unregister_class(OBJECT_OT_export_to_csv)
    bpy.utils.unregister_class(OBJECT_OT_create_example_piece)
    bpy.utils.unregister_class(OBJECT_PT_cortecloud_panel)
    bpy.utils.unregister_class(VIEW3D_PT_custom_panel)
    bpy.utils.unregister_class(OBJECT_OT_set_z_15)
    bpy.utils.unregister_class(OBJECT_OT_set_z_18)
    del bpy.types.Object.funcao_enum

if __name__ == "__main__":
    register()