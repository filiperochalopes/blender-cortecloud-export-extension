import bpy

# Definindo as opções da enumeração
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

# Registrar as classes e adicionar a propriedade ao iniciar o script
def register():
    bpy.utils.register_class(VIEW3D_PT_custom_panel)
    add_custom_enum_property()

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_custom_panel)
    del bpy.types.Object.funcao_enum

if __name__ == "__main__":
    register()