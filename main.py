bl_info = {
    "name": "CorteCloud Export Utils",
    "blender": (3, 0, 0),
    "category": "Object",
}

import bpy
import os
from bpy.props import StringProperty
import utils.create_item_custom_panel

# Function to configure the environment
def configure_environment(context):
    # Código de configuração do ambiente
    # Exemplo: Ajustar camadas, preparar cena
    print("Environment configuration completed")

# Function to create base materials
def create_base_materials(context):
    # Aqui você irá chamar o módulo Python externo que já possui
    # para criar os materiais base
    print("Base materials created")
    # Exemplo:
    # import_external_module_for_materials()

# Function to export CSV
def export_to_csv(filepath):
    # Utilizamos o código que você já tem para gerar o CSV
    # Adaptando para salvar no caminho selecionado
    print(f"Exporting to {filepath}")
    # Aqui você chama a função que você já criou para exportar CSV
    # Por exemplo: export_cut_list(filepath)



# Operator to configure environment
class OBJECT_OT_configure_environment(bpy.types.Operator):
    bl_idname = "object.configure_environment"
    bl_label = "Configure Environment"
    
    def execute(self, context):
        configure_environment(context)
        return {'FINISHED'}

# Operator to create base materials
class OBJECT_OT_create_base_materials(bpy.types.Operator):
    bl_idname = "object.create_base_materials"
    bl_label = "Create Base Materials"
    
    def execute(self, context):
        create_base_materials(context)
        return {'FINISHED'}

# Operator to export CSV
class OBJECT_OT_export_to_csv(bpy.types.Operator):
    bl_idname = "object.export_to_csv"
    bl_label = "Export to CSV"
    
    filepath: StringProperty(subtype="FILE_PATH")
    
    def execute(self, context):
        export_to_csv(self.filepath)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# Operator to create example piece
class OBJECT_OT_create_example_piece(bpy.types.Operator):
    bl_idname = "object.create_example_piece"
    bl_label = "Create Example Piece"
    
    def execute(self, context):
        create_example_piece(context)
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

# Registro das classes do plugin
def register():
    bpy.utils.register_class(OBJECT_OT_configure_environment)
    bpy.utils.register_class(OBJECT_OT_create_base_materials)
    bpy.utils.register_class(OBJECT_OT_export_to_csv)
    bpy.utils.register_class(OBJECT_OT_create_example_piece)
    bpy.utils.register_class(OBJECT_PT_cortecloud_panel)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_configure_environment)
    bpy.utils.unregister_class(OBJECT_OT_create_base_materials)
    bpy.utils.unregister_class(OBJECT_OT_export_to_csv)
    bpy.utils.unregister_class(OBJECT_OT_create_example_piece)
    bpy.utils.unregister_class(OBJECT_PT_cortecloud_panel)

if __name__ == "__main__":
    register()