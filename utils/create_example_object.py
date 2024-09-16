import bpy

# Function to create example piece (suspended drawer niche)
def create_example_piece(context):
    # Função que cria um nicho com gaveta suspensa
    bpy.ops.object.select_all(action='DESELECT')
    
    # Creating the niche (a box)
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
    niche = bpy.context.active_object
    niche.scale = (1, 0.5, 1)
    niche.name = "Niche"
    
    # Creating the suspended drawer (a smaller cube)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.5))
    drawer = bpy.context.active_object
    drawer.scale = (0.8, 0.4, 0.2)
    drawer.name = "Suspended Drawer"
    
    print("Example piece created: Niche with suspended drawer")