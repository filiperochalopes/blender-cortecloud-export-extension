"""
Por vezes, no CorteCloud, precisamos redefinir as funções de cada objeto e perdemos referência na etiqueta de impressões das peças pela GMAD. 
Uma opção é transformar as funções em complemento, para que a descrição de sua peça possa aparecer na etique ta e facilitar a montagem
"""

# Importando a API do blender
import bpy

# Capturar objetos selecionados
selection = bpy.context.selected_objects

# Adicionar e definir a propriedade 'comments' como uma string customizada
for obj in selection:
    # Verifica se o objeto já tem a propriedade 'comments'
    if "notes" not in obj:
        # Cria a propriedade 'notes' do tipo string no objeto
        obj["notes"] = obj.name
    else:
        # caso exista mantém a nota e adiciona o texto do nome após hífen
        obj["notes"] = f"{obj['notes']} - {obj.name}"

# Forçar a atualização da interface de propriedades para garantir que as propriedades sejam exibidas
bpy.context.view_layer.update()