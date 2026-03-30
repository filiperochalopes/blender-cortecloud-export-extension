# ruff: noqa: E402

bl_info = {
    "name": "CorteCloud Export Utils",
    "blender": (3, 0, 0),
    "category": "Object",
}

import bpy
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
    
    filepath: StringProperty(subtype="FILE_PATH")
    
    def execute(self, context):
        print(self.filepath)
        utils.export_to_csv(self.filepath)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        # Define o valor padrão do filepath no invoke, caso não esteja definido
        if not self.filepath:
            self.filepath = "cortecloud-cut-list.csv"
        
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# Operator para criar gaveta
class OBJECT_OT_create_drawer(bpy.types.Operator):
    bl_idname = "object.create_drawer"
    bl_label = "Create Drawer"
    
    def execute(self, context):
        utils.create_drawer(context)
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
        
        # Botão para criar gaveta
        layout.operator("object.create_drawer", text="Create Drawer")

func_options = [
    ('CONTRA_FRENTE_FUNDO_GAVETA', 'Contra Frente / Contra Fundo de Gaveta', ''),
    ('LATERAL_GAVETA', 'Lateral de Gaveta', ''),
    ('PORTA', 'Porta', ''),
    ('LATERAL_DIREITA', 'Lateral Direita', ''),
    ('LATERAL_ESQUERDA', 'Lateral Esquerda', ''),
    ('TAMPO', 'Tampo', ''),
    ('BASE', 'Base', ''),
]

# Função chamada quando a propriedade é alterada
def update_role_property(self, context):
    self["role"] = next((item[1] for item in func_options if item[0] == self.funcao_enum), "")  # Adiciona a função selecionada à propriedade 'role' do objeto

# Adicionando a propriedade de enumeração aos objetos do tipo Object
def add_custom_enum_property():
    bpy.types.Object.funcao_enum = bpy.props.EnumProperty(
        name="Role",
        description="Selecione a função da peça",
        items=func_options,
        default='BASE',
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
            if obj.type == 'MESH':
                layout.label(text=f"Material: {utils.get_object_main_material_name(obj)}")
                layout.label(text=f"Thickness: {utils.get_object_thickness_label(obj)}")
                layout.label(text=f"Edge Banding: {utils.get_object_edge_banding_label(obj)}")
            else:
                layout.label(text="Material: Not identified")
                layout.label(text="Thickness: Not identified")
                layout.label(text="Edge Banding: None")
            layout.prop(obj, "funcao_enum", text="Role")

# Registro das classes do plugin
def register():
    bpy.utils.register_class(OBJECT_OT_configure_environment)
    bpy.utils.register_class(OBJECT_OT_create_base_materials)
    bpy.utils.register_class(OBJECT_OT_export_to_csv)
    bpy.utils.register_class(OBJECT_OT_create_drawer)
    bpy.utils.register_class(OBJECT_PT_cortecloud_panel)
    bpy.utils.register_class(VIEW3D_PT_custom_panel)
    add_custom_enum_property()

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_configure_environment)
    bpy.utils.unregister_class(OBJECT_OT_create_base_materials)
    bpy.utils.unregister_class(OBJECT_OT_export_to_csv)
    bpy.utils.unregister_class(OBJECT_OT_create_drawer)
    bpy.utils.unregister_class(OBJECT_PT_cortecloud_panel)
    bpy.utils.unregister_class(VIEW3D_PT_custom_panel)
    del bpy.types.Object.funcao_enum

if __name__ == "__main__":
    register()
