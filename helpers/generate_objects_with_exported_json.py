import bpy
import bmesh
import json
from mathutils import Vector

DATA_JSON = r'''
{
  "meta": {
    "selected_count": 6,
    "scene_unit_system": "METRIC",
    "scene_scale_length": 0.0010000000474974513,
    "mm_factor": 1.0,
    "all_selected_are_mesh": true
  },
  "objects": [
    {
      "name": "Comoda - Gaveta - Base Inferior.003",
      "type": "MESH",
      "is_mesh": true,
      "dimensions_mm": {
        "x": 774.001,
        "y": 420.001,
        "z": 6.0
      },
      "cut_dimensions_mm": {
        "comprimento": 774.001,
        "largura": 420.001,
        "espessura": 6.0
      },
      "location_mm": {
        "x": 2292.004,
        "y": -1773.105,
        "z": 743.914
      },
      "rotation_deg": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
      },
      "scale": {
        "x": 1.0,
        "y": 1.0,
        "z": 1.0
      },
      "materials": [
        "White MDF",
        "Edge Banding (Com fita)",
        "No Edge Banding",
        "Edge Banding (Com fita)",
        "Edge Banding (Com fita)"
      ],
      "material_assignments": {
        "slots": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              4
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "No Edge Banding",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 3,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              3
            ],
            "used": true
          },
          {
            "slot_index": 4,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              1
            ],
            "used": true
          }
        ],
        "face_usage": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              4
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "No Edge Banding",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 3,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              3
            ],
            "used": true
          },
          {
            "slot_index": 4,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              1
            ],
            "used": true
          }
        ],
        "unused_slots": [],
        "faces": [
          {
            "polygon_index": 0,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 325080.5,
            "center_local_mm": {
              "x": 0.0,
              "y": 0.0,
              "z": -3.0
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1773.105,
              "z": 740.914
            },
            "normal_local": {
              "x": -0.0,
              "y": -0.0,
              "z": -1.0
            },
            "normal_world": {
              "x": -0.0,
              "y": -0.0,
              "z": -1.0
            },
            "face_signature": "z-@0.0,0.0,-3.0",
            "vertices_local_mm": [
              {
                "x": -387.001,
                "y": -210.0,
                "z": -3.0
              },
              {
                "x": -387.0,
                "y": 210.0,
                "z": -3.0
              },
              {
                "x": 387.001,
                "y": 210.0,
                "z": -3.0
              },
              {
                "x": 387.0,
                "y": -210.0,
                "z": -3.0
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1905.004,
                "y": -1983.105,
                "z": 740.914
              },
              {
                "x": 1905.004,
                "y": -1563.105,
                "z": 740.914
              },
              {
                "x": 2679.005,
                "y": -1563.106,
                "z": 740.914
              },
              {
                "x": 2679.005,
                "y": -1983.106,
                "z": 740.914
              }
            ]
          },
          {
            "polygon_index": 1,
            "material_index": 4,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 2519.929,
            "center_local_mm": {
              "x": 387.001,
              "y": -0.0,
              "z": -0.0
            },
            "center_world_mm": {
              "x": 2679.005,
              "y": -1773.106,
              "z": 743.914
            },
            "normal_local": {
              "x": 1.0,
              "y": -0.0,
              "z": 0.0
            },
            "normal_world": {
              "x": 1.0,
              "y": -0.0,
              "z": 0.0
            },
            "face_signature": "x+@387.0,-0.0,-0.0",
            "vertices_local_mm": [
              {
                "x": 387.0,
                "y": -210.0,
                "z": -3.0
              },
              {
                "x": 387.001,
                "y": 210.0,
                "z": -3.0
              },
              {
                "x": 387.001,
                "y": 210.0,
                "z": 3.0
              },
              {
                "x": 387.0,
                "y": -210.0,
                "z": 3.0
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2679.005,
                "y": -1983.106,
                "z": 740.914
              },
              {
                "x": 2679.005,
                "y": -1563.106,
                "z": 740.914
              },
              {
                "x": 2679.005,
                "y": -1563.106,
                "z": 746.913
              },
              {
                "x": 2679.005,
                "y": -1983.106,
                "z": 746.913
              }
            ]
          },
          {
            "polygon_index": 2,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 325080.5,
            "center_local_mm": {
              "x": 0.0,
              "y": 0.0,
              "z": 3.0
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1773.105,
              "z": 746.914
            },
            "normal_local": {
              "x": 0.0,
              "y": 0.0,
              "z": 1.0
            },
            "normal_world": {
              "x": 0.0,
              "y": 0.0,
              "z": 1.0
            },
            "face_signature": "z+@0.0,0.0,3.0",
            "vertices_local_mm": [
              {
                "x": 387.0,
                "y": -210.0,
                "z": 3.0
              },
              {
                "x": 387.001,
                "y": 210.0,
                "z": 3.0
              },
              {
                "x": -387.0,
                "y": 210.0,
                "z": 3.0
              },
              {
                "x": -387.001,
                "y": -210.0,
                "z": 3.0
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2679.005,
                "y": -1983.106,
                "z": 746.913
              },
              {
                "x": 2679.005,
                "y": -1563.106,
                "z": 746.913
              },
              {
                "x": 1905.004,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 1905.004,
                "y": -1983.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 3,
            "material_index": 3,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 2519.929,
            "center_local_mm": {
              "x": -387.0,
              "y": 0.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 1905.004,
              "y": -1773.105,
              "z": 743.914
            },
            "normal_local": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "normal_world": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "face_signature": "x-@-387.0,0.0,0.0",
            "vertices_local_mm": [
              {
                "x": -387.001,
                "y": -210.0,
                "z": 3.0
              },
              {
                "x": -387.0,
                "y": 210.0,
                "z": 3.0
              },
              {
                "x": -387.0,
                "y": 210.0,
                "z": -3.0
              },
              {
                "x": -387.001,
                "y": -210.0,
                "z": -3.0
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1905.004,
                "y": -1983.105,
                "z": 746.914
              },
              {
                "x": 1905.004,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 1905.004,
                "y": -1563.105,
                "z": 740.914
              },
              {
                "x": 1905.004,
                "y": -1983.105,
                "z": 740.914
              }
            ]
          },
          {
            "polygon_index": 4,
            "material_index": 1,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 4643.873,
            "center_local_mm": {
              "x": -0.0,
              "y": -210.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1983.105,
              "z": 743.914
            },
            "normal_local": {
              "x": -0.0,
              "y": -1.0,
              "z": 0.0
            },
            "normal_world": {
              "x": -0.0,
              "y": -1.0,
              "z": 0.0
            },
            "face_signature": "y-@-0.0,-210.0,0.0",
            "vertices_local_mm": [
              {
                "x": 387.0,
                "y": -210.0,
                "z": -3.0
              },
              {
                "x": 387.0,
                "y": -210.0,
                "z": 3.0
              },
              {
                "x": -387.001,
                "y": -210.0,
                "z": 3.0
              },
              {
                "x": -387.001,
                "y": -210.0,
                "z": -3.0
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2679.005,
                "y": -1983.106,
                "z": 740.914
              },
              {
                "x": 2679.005,
                "y": -1983.106,
                "z": 746.913
              },
              {
                "x": 1905.004,
                "y": -1983.105,
                "z": 746.914
              },
              {
                "x": 1905.004,
                "y": -1983.105,
                "z": 740.914
              }
            ]
          },
          {
            "polygon_index": 5,
            "material_index": 2,
            "material": "No Edge Banding",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 4643.873,
            "center_local_mm": {
              "x": 0.0,
              "y": 210.0,
              "z": -0.0
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1563.105,
              "z": 743.914
            },
            "normal_local": {
              "x": 0.0,
              "y": 1.0,
              "z": 0.0
            },
            "normal_world": {
              "x": 0.0,
              "y": 1.0,
              "z": 0.0
            },
            "face_signature": "y+@0.0,210.0,-0.0",
            "vertices_local_mm": [
              {
                "x": 387.001,
                "y": 210.0,
                "z": 3.0
              },
              {
                "x": 387.001,
                "y": 210.0,
                "z": -3.0
              },
              {
                "x": -387.0,
                "y": 210.0,
                "z": -3.0
              },
              {
                "x": -387.0,
                "y": 210.0,
                "z": 3.0
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2679.005,
                "y": -1563.106,
                "z": 746.913
              },
              {
                "x": 2679.005,
                "y": -1563.106,
                "z": 740.914
              },
              {
                "x": 1905.004,
                "y": -1563.105,
                "z": 740.914
              },
              {
                "x": 1905.004,
                "y": -1563.105,
                "z": 746.914
              }
            ]
          }
        ]
      },
      "custom_props": {
        "notes": "Fachada Armário - Tampo Lateral.001"
      }
    },
    {
      "name": "Comoda - Gaveta - Fundo.003",
      "type": "MESH",
      "is_mesh": true,
      "dimensions_mm": {
        "x": 744.001,
        "y": 15.0,
        "z": 187.016
      },
      "cut_dimensions_mm": {
        "comprimento": 744.001,
        "largura": 187.016,
        "espessura": 15.0
      },
      "location_mm": {
        "x": 2292.004,
        "y": -1975.606,
        "z": 840.422
      },
      "rotation_deg": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
      },
      "scale": {
        "x": 1.0,
        "y": 1.0,
        "z": 1.0
      },
      "materials": [
        "White MDF",
        "Edge Banding (Com fita)",
        "No Edge Banding"
      ],
      "material_assignments": {
        "slots": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "No Edge Banding",
            "face_count": 3,
            "polygon_indices": [
              1,
              3,
              4
            ],
            "used": true
          }
        ],
        "face_usage": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "No Edge Banding",
            "face_count": 3,
            "polygon_indices": [
              1,
              3,
              4
            ],
            "used": true
          }
        ],
        "unused_slots": [],
        "faces": [
          {
            "polygon_index": 0,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 139140.138,
            "center_local_mm": {
              "x": 0.0,
              "y": 7.5,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1968.106,
              "z": 840.422
            },
            "normal_local": {
              "x": -0.0,
              "y": 1.0,
              "z": -0.0
            },
            "normal_world": {
              "x": -0.0,
              "y": 1.0,
              "z": -0.0
            },
            "face_signature": "y+@0.0,7.5,0.0",
            "vertices_local_mm": [
              {
                "x": -372.001,
                "y": 7.5,
                "z": -93.508
              },
              {
                "x": -372.0,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": 372.001,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": 372.0,
                "y": 7.5,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1920.004,
                "y": -1968.106,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1968.106,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1968.106,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1968.106,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 1,
            "material_index": 2,
            "material": "No Edge Banding",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 2805.183,
            "center_local_mm": {
              "x": 372.001,
              "y": 0.0,
              "z": -0.0
            },
            "center_world_mm": {
              "x": 2664.005,
              "y": -1975.605,
              "z": 840.422
            },
            "normal_local": {
              "x": 1.0,
              "y": 0.0,
              "z": -0.0
            },
            "normal_world": {
              "x": 1.0,
              "y": 0.0,
              "z": -0.0
            },
            "face_signature": "x+@372.0,0.0,-0.0",
            "vertices_local_mm": [
              {
                "x": 372.0,
                "y": 7.5,
                "z": -93.508
              },
              {
                "x": 372.001,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": 372.001,
                "y": -7.5,
                "z": 93.508
              },
              {
                "x": 372.0,
                "y": -7.5,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.005,
                "y": -1968.106,
                "z": 746.914
              },
              {
                "x": 2664.005,
                "y": -1968.106,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1983.105,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1983.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 2,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 139140.138,
            "center_local_mm": {
              "x": 0.0,
              "y": -7.5,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1983.106,
              "z": 840.422
            },
            "normal_local": {
              "x": 0.0,
              "y": -1.0,
              "z": 0.0
            },
            "normal_world": {
              "x": 0.0,
              "y": -1.0,
              "z": 0.0
            },
            "face_signature": "y-@0.0,-7.5,0.0",
            "vertices_local_mm": [
              {
                "x": 372.0,
                "y": -7.5,
                "z": -93.508
              },
              {
                "x": 372.001,
                "y": -7.5,
                "z": 93.508
              },
              {
                "x": -372.0,
                "y": -7.5,
                "z": 93.508
              },
              {
                "x": -372.001,
                "y": -7.5,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.005,
                "y": -1983.105,
                "z": 746.914
              },
              {
                "x": 2664.005,
                "y": -1983.105,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1983.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1983.106,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 3,
            "material_index": 2,
            "material": "No Edge Banding",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 2805.182,
            "center_local_mm": {
              "x": -372.0,
              "y": -0.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 1920.004,
              "y": -1975.606,
              "z": 840.422
            },
            "normal_local": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "normal_world": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "face_signature": "x-@-372.0,-0.0,0.0",
            "vertices_local_mm": [
              {
                "x": -372.001,
                "y": -7.5,
                "z": -93.508
              },
              {
                "x": -372.0,
                "y": -7.5,
                "z": 93.508
              },
              {
                "x": -372.0,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": -372.001,
                "y": 7.5,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1920.004,
                "y": -1983.106,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1983.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1968.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1968.106,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 4,
            "material_index": 2,
            "material": "No Edge Banding",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 11159.782,
            "center_local_mm": {
              "x": -0.0,
              "y": -0.0,
              "z": -93.508
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1975.606,
              "z": 746.914
            },
            "normal_local": {
              "x": -0.0,
              "y": 0.0,
              "z": -1.0
            },
            "normal_world": {
              "x": -0.0,
              "y": 0.0,
              "z": -1.0
            },
            "face_signature": "z-@-0.0,-0.0,-93.508",
            "vertices_local_mm": [
              {
                "x": 372.0,
                "y": 7.5,
                "z": -93.508
              },
              {
                "x": 372.0,
                "y": -7.5,
                "z": -93.508
              },
              {
                "x": -372.001,
                "y": -7.5,
                "z": -93.508
              },
              {
                "x": -372.001,
                "y": 7.5,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.005,
                "y": -1968.106,
                "z": 746.914
              },
              {
                "x": 2664.005,
                "y": -1983.105,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1983.106,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1968.106,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 5,
            "material_index": 1,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 11159.784,
            "center_local_mm": {
              "x": 0.0,
              "y": 0.0,
              "z": 93.508
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1975.606,
              "z": 933.93
            },
            "normal_local": {
              "x": 0.0,
              "y": 0.0,
              "z": 1.0
            },
            "normal_world": {
              "x": 0.0,
              "y": 0.0,
              "z": 1.0
            },
            "face_signature": "z+@0.0,0.0,93.508",
            "vertices_local_mm": [
              {
                "x": 372.001,
                "y": -7.5,
                "z": 93.508
              },
              {
                "x": 372.001,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": -372.0,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": -372.0,
                "y": -7.5,
                "z": 93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.005,
                "y": -1983.105,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1968.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1968.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1983.106,
                "z": 933.93
              }
            ]
          }
        ]
      },
      "custom_props": {
        "notes": "Fachada Armário - Tampo Lateral.001"
      }
    },
    {
      "name": "Comoda - Gaveta - Frente.003",
      "type": "MESH",
      "is_mesh": true,
      "dimensions_mm": {
        "x": 826.001,
        "y": 15.0,
        "z": 222.017
      },
      "cut_dimensions_mm": {
        "comprimento": 826.001,
        "largura": 222.017,
        "espessura": 15.0
      },
      "location_mm": {
        "x": 2292.004,
        "y": -1555.605,
        "z": 832.922
      },
      "rotation_deg": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
      },
      "scale": {
        "x": 1.0,
        "y": 1.0,
        "z": 1.0
      },
      "materials": [
        "White MDF",
        "Edge Banding (Com fita)",
        "Edge Banding (Com fita)",
        "Edge Banding (Com fita)",
        "Edge Banding (Com fita)"
      ],
      "material_assignments": {
        "slots": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              4
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 3,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              3
            ],
            "used": true
          },
          {
            "slot_index": 4,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              1
            ],
            "used": true
          }
        ],
        "face_usage": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              4
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 3,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              3
            ],
            "used": true
          },
          {
            "slot_index": 4,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              1
            ],
            "used": true
          }
        ],
        "unused_slots": [],
        "faces": [
          {
            "polygon_index": 0,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 183385.486,
            "center_local_mm": {
              "x": 0.0,
              "y": 7.5,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1548.105,
              "z": 832.922
            },
            "normal_local": {
              "x": -0.0,
              "y": 1.0,
              "z": -0.0
            },
            "normal_world": {
              "x": -0.0,
              "y": 1.0,
              "z": -0.0
            },
            "face_signature": "y+@0.0,7.5,0.0",
            "vertices_local_mm": [
              {
                "x": -413.0,
                "y": 7.5,
                "z": -111.008
              },
              {
                "x": -413.0,
                "y": 7.5,
                "z": 111.008
              },
              {
                "x": 413.0,
                "y": 7.5,
                "z": 111.008
              },
              {
                "x": 413.0,
                "y": 7.5,
                "z": -111.008
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1879.004,
                "y": -1548.106,
                "z": 721.914
              },
              {
                "x": 1879.004,
                "y": -1548.106,
                "z": 943.93
              },
              {
                "x": 2705.004,
                "y": -1548.105,
                "z": 943.93
              },
              {
                "x": 2705.004,
                "y": -1548.105,
                "z": 721.913
              }
            ]
          },
          {
            "polygon_index": 1,
            "material_index": 4,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 3330.174,
            "center_local_mm": {
              "x": 413.0,
              "y": 0.0,
              "z": -0.0
            },
            "center_world_mm": {
              "x": 2705.004,
              "y": -1555.605,
              "z": 832.922
            },
            "normal_local": {
              "x": 1.0,
              "y": 0.0,
              "z": -0.0
            },
            "normal_world": {
              "x": 1.0,
              "y": 0.0,
              "z": -0.0
            },
            "face_signature": "x+@413.0,0.0,-0.0",
            "vertices_local_mm": [
              {
                "x": 413.0,
                "y": 7.5,
                "z": -111.008
              },
              {
                "x": 413.0,
                "y": 7.5,
                "z": 111.008
              },
              {
                "x": 413.0,
                "y": -7.5,
                "z": 111.008
              },
              {
                "x": 413.0,
                "y": -7.5,
                "z": -111.008
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2705.004,
                "y": -1548.105,
                "z": 721.913
              },
              {
                "x": 2705.004,
                "y": -1548.105,
                "z": 943.93
              },
              {
                "x": 2705.004,
                "y": -1563.105,
                "z": 943.93
              },
              {
                "x": 2705.004,
                "y": -1563.105,
                "z": 721.913
              }
            ]
          },
          {
            "polygon_index": 2,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 183385.486,
            "center_local_mm": {
              "x": 0.0,
              "y": -7.5,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1563.105,
              "z": 832.922
            },
            "normal_local": {
              "x": 0.0,
              "y": -1.0,
              "z": 0.0
            },
            "normal_world": {
              "x": 0.0,
              "y": -1.0,
              "z": 0.0
            },
            "face_signature": "y-@0.0,-7.5,0.0",
            "vertices_local_mm": [
              {
                "x": 413.0,
                "y": -7.5,
                "z": -111.008
              },
              {
                "x": 413.0,
                "y": -7.5,
                "z": 111.008
              },
              {
                "x": -413.0,
                "y": -7.5,
                "z": 111.008
              },
              {
                "x": -413.0,
                "y": -7.5,
                "z": -111.008
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2705.004,
                "y": -1563.105,
                "z": 721.913
              },
              {
                "x": 2705.004,
                "y": -1563.105,
                "z": 943.93
              },
              {
                "x": 1879.004,
                "y": -1563.105,
                "z": 943.93
              },
              {
                "x": 1879.004,
                "y": -1563.105,
                "z": 721.914
              }
            ]
          },
          {
            "polygon_index": 3,
            "material_index": 3,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 3330.174,
            "center_local_mm": {
              "x": -413.0,
              "y": -0.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 1879.004,
              "y": -1555.606,
              "z": 832.922
            },
            "normal_local": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "normal_world": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "face_signature": "x-@-413.0,-0.0,0.0",
            "vertices_local_mm": [
              {
                "x": -413.0,
                "y": -7.5,
                "z": -111.008
              },
              {
                "x": -413.0,
                "y": -7.5,
                "z": 111.008
              },
              {
                "x": -413.0,
                "y": 7.5,
                "z": 111.008
              },
              {
                "x": -413.0,
                "y": 7.5,
                "z": -111.008
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1879.004,
                "y": -1563.105,
                "z": 721.914
              },
              {
                "x": 1879.004,
                "y": -1563.105,
                "z": 943.93
              },
              {
                "x": 1879.004,
                "y": -1548.106,
                "z": 943.93
              },
              {
                "x": 1879.004,
                "y": -1548.106,
                "z": 721.914
              }
            ]
          },
          {
            "polygon_index": 4,
            "material_index": 1,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 12389.747,
            "center_local_mm": {
              "x": -0.0,
              "y": -0.0,
              "z": -111.008
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1555.605,
              "z": 721.914
            },
            "normal_local": {
              "x": -0.0,
              "y": 0.0,
              "z": -1.0
            },
            "normal_world": {
              "x": -0.0,
              "y": 0.0,
              "z": -1.0
            },
            "face_signature": "z-@-0.0,-0.0,-111.008",
            "vertices_local_mm": [
              {
                "x": 413.0,
                "y": 7.5,
                "z": -111.008
              },
              {
                "x": 413.0,
                "y": -7.5,
                "z": -111.008
              },
              {
                "x": -413.0,
                "y": -7.5,
                "z": -111.008
              },
              {
                "x": -413.0,
                "y": 7.5,
                "z": -111.008
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2705.004,
                "y": -1548.105,
                "z": 721.913
              },
              {
                "x": 2705.004,
                "y": -1563.105,
                "z": 721.913
              },
              {
                "x": 1879.004,
                "y": -1563.105,
                "z": 721.914
              },
              {
                "x": 1879.004,
                "y": -1548.106,
                "z": 721.914
              }
            ]
          },
          {
            "polygon_index": 5,
            "material_index": 2,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 12389.749,
            "center_local_mm": {
              "x": 0.0,
              "y": 0.0,
              "z": 111.008
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1555.605,
              "z": 943.93
            },
            "normal_local": {
              "x": 0.0,
              "y": 0.0,
              "z": 1.0
            },
            "normal_world": {
              "x": 0.0,
              "y": 0.0,
              "z": 1.0
            },
            "face_signature": "z+@0.0,0.0,111.008",
            "vertices_local_mm": [
              {
                "x": 413.0,
                "y": -7.5,
                "z": 111.008
              },
              {
                "x": 413.0,
                "y": 7.5,
                "z": 111.008
              },
              {
                "x": -413.0,
                "y": 7.5,
                "z": 111.008
              },
              {
                "x": -413.0,
                "y": -7.5,
                "z": 111.008
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2705.004,
                "y": -1563.105,
                "z": 943.93
              },
              {
                "x": 2705.004,
                "y": -1548.105,
                "z": 943.93
              },
              {
                "x": 1879.004,
                "y": -1548.106,
                "z": 943.93
              },
              {
                "x": 1879.004,
                "y": -1563.105,
                "z": 943.93
              }
            ]
          }
        ]
      },
      "custom_props": {
        "notes": "Fachada Armário - Tampo Lateral.001"
      }
    },
    {
      "name": "Comoda - Gaveta - Lateral.006",
      "type": "MESH",
      "is_mesh": true,
      "dimensions_mm": {
        "x": 15.0,
        "y": 420.001,
        "z": 187.016
      },
      "cut_dimensions_mm": {
        "comprimento": 420.001,
        "largura": 187.016,
        "espessura": 15.0
      },
      "location_mm": {
        "x": 2671.505,
        "y": -1773.105,
        "z": 840.422
      },
      "rotation_deg": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
      },
      "scale": {
        "x": 1.0,
        "y": 1.0,
        "z": 1.0
      },
      "materials": [
        "White MDF",
        "Edge Banding (Com fita)",
        "No Edge Banding",
        "Edge Banding (Com fita)",
        "Edge Banding (Com fita)"
      ],
      "material_assignments": {
        "slots": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              4
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "No Edge Banding",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 3,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              3
            ],
            "used": true
          },
          {
            "slot_index": 4,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              1
            ],
            "used": true
          }
        ],
        "face_usage": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              4
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "No Edge Banding",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 3,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              3
            ],
            "used": true
          },
          {
            "slot_index": 4,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              1
            ],
            "used": true
          }
        ],
        "unused_slots": [],
        "faces": [
          {
            "polygon_index": 0,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 78546.742,
            "center_local_mm": {
              "x": 7.5,
              "y": 0.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 2679.004,
              "y": -1773.105,
              "z": 840.422
            },
            "normal_local": {
              "x": 1.0,
              "y": -0.0,
              "z": -0.0
            },
            "normal_world": {
              "x": 1.0,
              "y": -0.0,
              "z": -0.0
            },
            "face_signature": "x+@7.5,0.0,0.0",
            "vertices_local_mm": [
              {
                "x": 7.5,
                "y": -210.0,
                "z": -93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": -93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": 7.5,
                "y": -210.0,
                "z": 93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2679.004,
                "y": -1983.105,
                "z": 746.914
              },
              {
                "x": 2679.004,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 2679.005,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 2679.005,
                "y": -1983.106,
                "z": 933.93
              }
            ]
          },
          {
            "polygon_index": 1,
            "material_index": 4,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 6299.871,
            "center_local_mm": {
              "x": 0.0,
              "y": -0.0,
              "z": 93.508
            },
            "center_world_mm": {
              "x": 2671.505,
              "y": -1773.106,
              "z": 933.93
            },
            "normal_local": {
              "x": 0.0,
              "y": -0.0,
              "z": 1.0
            },
            "normal_world": {
              "x": 0.0,
              "y": -0.0,
              "z": 1.0
            },
            "face_signature": "z+@0.0,-0.0,93.508",
            "vertices_local_mm": [
              {
                "x": 7.5,
                "y": -210.0,
                "z": 93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": -210.0,
                "z": 93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2679.005,
                "y": -1983.106,
                "z": 933.93
              },
              {
                "x": 2679.005,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1983.106,
                "z": 933.93
              }
            ]
          },
          {
            "polygon_index": 2,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 78546.742,
            "center_local_mm": {
              "x": -7.5,
              "y": 0.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 2664.005,
              "y": -1773.105,
              "z": 840.422
            },
            "normal_local": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "normal_world": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "face_signature": "x-@-7.5,0.0,0.0",
            "vertices_local_mm": [
              {
                "x": -7.5,
                "y": -210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": 210.0,
                "z": -93.508
              },
              {
                "x": -7.5,
                "y": -210.0,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.005,
                "y": -1983.106,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 2664.004,
                "y": -1983.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 3,
            "material_index": 3,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 6299.871,
            "center_local_mm": {
              "x": -0.0,
              "y": 0.0,
              "z": -93.508
            },
            "center_world_mm": {
              "x": 2671.504,
              "y": -1773.105,
              "z": 746.914
            },
            "normal_local": {
              "x": 0.0,
              "y": 0.0,
              "z": -1.0
            },
            "normal_world": {
              "x": 0.0,
              "y": 0.0,
              "z": -1.0
            },
            "face_signature": "z-@-0.0,0.0,-93.508",
            "vertices_local_mm": [
              {
                "x": -7.5,
                "y": -210.0,
                "z": -93.508
              },
              {
                "x": -7.5,
                "y": 210.0,
                "z": -93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": -93.508
              },
              {
                "x": 7.5,
                "y": -210.0,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.004,
                "y": -1983.105,
                "z": 746.914
              },
              {
                "x": 2664.005,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 2679.004,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 2679.004,
                "y": -1983.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 4,
            "material_index": 1,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 2805.182,
            "center_local_mm": {
              "x": -0.0,
              "y": -210.0,
              "z": -0.0
            },
            "center_world_mm": {
              "x": 2671.505,
              "y": -1983.105,
              "z": 840.422
            },
            "normal_local": {
              "x": 0.0,
              "y": -1.0,
              "z": -0.0
            },
            "normal_world": {
              "x": 0.0,
              "y": -1.0,
              "z": -0.0
            },
            "face_signature": "y-@-0.0,-210.0,-0.0",
            "vertices_local_mm": [
              {
                "x": 7.5,
                "y": -210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": -210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": -210.0,
                "z": -93.508
              },
              {
                "x": 7.5,
                "y": -210.0,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2679.005,
                "y": -1983.106,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1983.106,
                "z": 933.93
              },
              {
                "x": 2664.004,
                "y": -1983.105,
                "z": 746.914
              },
              {
                "x": 2679.004,
                "y": -1983.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 5,
            "material_index": 2,
            "material": "No Edge Banding",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 2805.182,
            "center_local_mm": {
              "x": 0.0,
              "y": 210.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 2671.505,
              "y": -1563.105,
              "z": 840.422
            },
            "normal_local": {
              "x": 0.0,
              "y": 1.0,
              "z": 0.0
            },
            "normal_world": {
              "x": 0.0,
              "y": 1.0,
              "z": 0.0
            },
            "face_signature": "y+@0.0,210.0,0.0",
            "vertices_local_mm": [
              {
                "x": -7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": -93.508
              },
              {
                "x": -7.5,
                "y": 210.0,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.005,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 2679.005,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 2679.004,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 2664.005,
                "y": -1563.105,
                "z": 746.914
              }
            ]
          }
        ]
      },
      "custom_props": {
        "notes": "Fachada Armário - Tampo Lateral.001"
      }
    },
    {
      "name": "Comoda - Gaveta - Lateral.007",
      "type": "MESH",
      "is_mesh": true,
      "dimensions_mm": {
        "x": 15.0,
        "y": 420.001,
        "z": 187.016
      },
      "cut_dimensions_mm": {
        "comprimento": 420.001,
        "largura": 187.016,
        "espessura": 15.0
      },
      "location_mm": {
        "x": 1912.504,
        "y": -1773.105,
        "z": 840.422
      },
      "rotation_deg": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
      },
      "scale": {
        "x": 1.0,
        "y": 1.0,
        "z": 1.0
      },
      "materials": [
        "White MDF",
        "Edge Banding (Com fita)",
        "No Edge Banding",
        "Edge Banding (Com fita)",
        "Edge Banding (Com fita)"
      ],
      "material_assignments": {
        "slots": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              4
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "No Edge Banding",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 3,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              3
            ],
            "used": true
          },
          {
            "slot_index": 4,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              1
            ],
            "used": true
          }
        ],
        "face_usage": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              4
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "No Edge Banding",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 3,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              3
            ],
            "used": true
          },
          {
            "slot_index": 4,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              1
            ],
            "used": true
          }
        ],
        "unused_slots": [],
        "faces": [
          {
            "polygon_index": 0,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 78546.742,
            "center_local_mm": {
              "x": 7.5,
              "y": 0.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 1920.004,
              "y": -1773.105,
              "z": 840.422
            },
            "normal_local": {
              "x": 1.0,
              "y": -0.0,
              "z": -0.0
            },
            "normal_world": {
              "x": 1.0,
              "y": -0.0,
              "z": -0.0
            },
            "face_signature": "x+@7.5,0.0,0.0",
            "vertices_local_mm": [
              {
                "x": 7.5,
                "y": -210.0,
                "z": -93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": -93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": 7.5,
                "y": -210.0,
                "z": 93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1920.003,
                "y": -1983.105,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1983.106,
                "z": 933.93
              }
            ]
          },
          {
            "polygon_index": 1,
            "material_index": 4,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 6299.871,
            "center_local_mm": {
              "x": 0.0,
              "y": -0.0,
              "z": 93.508
            },
            "center_world_mm": {
              "x": 1912.504,
              "y": -1773.106,
              "z": 933.93
            },
            "normal_local": {
              "x": 0.0,
              "y": -0.0,
              "z": 1.0
            },
            "normal_world": {
              "x": 0.0,
              "y": -0.0,
              "z": 1.0
            },
            "face_signature": "z+@0.0,-0.0,93.508",
            "vertices_local_mm": [
              {
                "x": 7.5,
                "y": -210.0,
                "z": 93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": -210.0,
                "z": 93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1920.004,
                "y": -1983.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 1905.004,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 1905.004,
                "y": -1983.106,
                "z": 933.93
              }
            ]
          },
          {
            "polygon_index": 2,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 78546.742,
            "center_local_mm": {
              "x": -7.5,
              "y": 0.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 1905.004,
              "y": -1773.105,
              "z": 840.422
            },
            "normal_local": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "normal_world": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "face_signature": "x-@-7.5,0.0,0.0",
            "vertices_local_mm": [
              {
                "x": -7.5,
                "y": -210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": 210.0,
                "z": -93.508
              },
              {
                "x": -7.5,
                "y": -210.0,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1905.004,
                "y": -1983.106,
                "z": 933.93
              },
              {
                "x": 1905.004,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 1905.004,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 1905.004,
                "y": -1983.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 3,
            "material_index": 3,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 6299.871,
            "center_local_mm": {
              "x": -0.0,
              "y": 0.0,
              "z": -93.508
            },
            "center_world_mm": {
              "x": 1912.504,
              "y": -1773.105,
              "z": 746.914
            },
            "normal_local": {
              "x": 0.0,
              "y": 0.0,
              "z": -1.0
            },
            "normal_world": {
              "x": 0.0,
              "y": 0.0,
              "z": -1.0
            },
            "face_signature": "z-@-0.0,0.0,-93.508",
            "vertices_local_mm": [
              {
                "x": -7.5,
                "y": -210.0,
                "z": -93.508
              },
              {
                "x": -7.5,
                "y": 210.0,
                "z": -93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": -93.508
              },
              {
                "x": 7.5,
                "y": -210.0,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1905.004,
                "y": -1983.105,
                "z": 746.914
              },
              {
                "x": 1905.004,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 1920.003,
                "y": -1983.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 4,
            "material_index": 1,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 2805.182,
            "center_local_mm": {
              "x": -0.0,
              "y": -210.0,
              "z": -0.0
            },
            "center_world_mm": {
              "x": 1912.504,
              "y": -1983.105,
              "z": 840.422
            },
            "normal_local": {
              "x": 0.0,
              "y": -1.0,
              "z": -0.0
            },
            "normal_world": {
              "x": 0.0,
              "y": -1.0,
              "z": -0.0
            },
            "face_signature": "y-@-0.0,-210.0,-0.0",
            "vertices_local_mm": [
              {
                "x": 7.5,
                "y": -210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": -210.0,
                "z": 93.508
              },
              {
                "x": -7.5,
                "y": -210.0,
                "z": -93.508
              },
              {
                "x": 7.5,
                "y": -210.0,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1920.004,
                "y": -1983.106,
                "z": 933.93
              },
              {
                "x": 1905.004,
                "y": -1983.106,
                "z": 933.93
              },
              {
                "x": 1905.004,
                "y": -1983.105,
                "z": 746.914
              },
              {
                "x": 1920.003,
                "y": -1983.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 5,
            "material_index": 2,
            "material": "No Edge Banding",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 2805.182,
            "center_local_mm": {
              "x": 0.0,
              "y": 210.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 1912.504,
              "y": -1563.105,
              "z": 840.422
            },
            "normal_local": {
              "x": 0.0,
              "y": 1.0,
              "z": 0.0
            },
            "normal_world": {
              "x": 0.0,
              "y": 1.0,
              "z": 0.0
            },
            "face_signature": "y+@0.0,210.0,0.0",
            "vertices_local_mm": [
              {
                "x": -7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": 93.508
              },
              {
                "x": 7.5,
                "y": 210.0,
                "z": -93.508
              },
              {
                "x": -7.5,
                "y": 210.0,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1905.004,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 1905.004,
                "y": -1563.105,
                "z": 746.914
              }
            ]
          }
        ]
      },
      "custom_props": {
        "notes": "Fachada Armário - Tampo Lateral.001"
      }
    },
    {
      "name": "Comoda - Gaveta - Contra Frente.003",
      "type": "MESH",
      "is_mesh": true,
      "dimensions_mm": {
        "x": 744.001,
        "y": 15.0,
        "z": 187.016
      },
      "cut_dimensions_mm": {
        "comprimento": 744.001,
        "largura": 187.016,
        "espessura": 15.0
      },
      "location_mm": {
        "x": 2292.004,
        "y": -1570.605,
        "z": 840.422
      },
      "rotation_deg": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
      },
      "scale": {
        "x": 1.0,
        "y": 1.0,
        "z": 1.0
      },
      "materials": [
        "White MDF",
        "Edge Banding (Com fita)",
        "No Edge Banding"
      ],
      "material_assignments": {
        "slots": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "No Edge Banding",
            "face_count": 3,
            "polygon_indices": [
              1,
              3,
              4
            ],
            "used": true
          }
        ],
        "face_usage": [
          {
            "slot_index": 0,
            "material": "White MDF",
            "face_count": 2,
            "polygon_indices": [
              0,
              2
            ],
            "used": true
          },
          {
            "slot_index": 1,
            "material": "Edge Banding (Com fita)",
            "face_count": 1,
            "polygon_indices": [
              5
            ],
            "used": true
          },
          {
            "slot_index": 2,
            "material": "No Edge Banding",
            "face_count": 3,
            "polygon_indices": [
              1,
              3,
              4
            ],
            "used": true
          }
        ],
        "unused_slots": [],
        "faces": [
          {
            "polygon_index": 0,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 139140.138,
            "center_local_mm": {
              "x": 0.0,
              "y": 7.5,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1563.105,
              "z": 840.422
            },
            "normal_local": {
              "x": -0.0,
              "y": 1.0,
              "z": -0.0
            },
            "normal_world": {
              "x": -0.0,
              "y": 1.0,
              "z": -0.0
            },
            "face_signature": "y+@0.0,7.5,0.0",
            "vertices_local_mm": [
              {
                "x": -372.001,
                "y": 7.5,
                "z": -93.508
              },
              {
                "x": -372.0,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": 372.001,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": 372.0,
                "y": 7.5,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1920.004,
                "y": -1563.106,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1563.105,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1563.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 1,
            "material_index": 2,
            "material": "No Edge Banding",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 2805.183,
            "center_local_mm": {
              "x": 372.001,
              "y": 0.0,
              "z": -0.0
            },
            "center_world_mm": {
              "x": 2664.005,
              "y": -1570.605,
              "z": 840.422
            },
            "normal_local": {
              "x": 1.0,
              "y": 0.0,
              "z": -0.0
            },
            "normal_world": {
              "x": 1.0,
              "y": 0.0,
              "z": -0.0
            },
            "face_signature": "x+@372.0,0.0,-0.0",
            "vertices_local_mm": [
              {
                "x": 372.0,
                "y": 7.5,
                "z": -93.508
              },
              {
                "x": 372.001,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": 372.001,
                "y": -7.5,
                "z": 93.508
              },
              {
                "x": 372.0,
                "y": -7.5,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.005,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 2664.005,
                "y": -1563.105,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1578.105,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1578.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 2,
            "material_index": 0,
            "material": "White MDF",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 139140.138,
            "center_local_mm": {
              "x": 0.0,
              "y": -7.5,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1578.105,
              "z": 840.422
            },
            "normal_local": {
              "x": 0.0,
              "y": -1.0,
              "z": 0.0
            },
            "normal_world": {
              "x": 0.0,
              "y": -1.0,
              "z": 0.0
            },
            "face_signature": "y-@0.0,-7.5,0.0",
            "vertices_local_mm": [
              {
                "x": 372.0,
                "y": -7.5,
                "z": -93.508
              },
              {
                "x": 372.001,
                "y": -7.5,
                "z": 93.508
              },
              {
                "x": -372.0,
                "y": -7.5,
                "z": 93.508
              },
              {
                "x": -372.001,
                "y": -7.5,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.005,
                "y": -1578.105,
                "z": 746.914
              },
              {
                "x": 2664.005,
                "y": -1578.105,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1578.105,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1578.105,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 3,
            "material_index": 2,
            "material": "No Edge Banding",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 2805.182,
            "center_local_mm": {
              "x": -372.0,
              "y": -0.0,
              "z": 0.0
            },
            "center_world_mm": {
              "x": 1920.004,
              "y": -1570.606,
              "z": 840.422
            },
            "normal_local": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "normal_world": {
              "x": -1.0,
              "y": 0.0,
              "z": 0.0
            },
            "face_signature": "x-@-372.0,-0.0,0.0",
            "vertices_local_mm": [
              {
                "x": -372.001,
                "y": -7.5,
                "z": -93.508
              },
              {
                "x": -372.0,
                "y": -7.5,
                "z": 93.508
              },
              {
                "x": -372.0,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": -372.001,
                "y": 7.5,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 1920.004,
                "y": -1578.105,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1578.105,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1563.106,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 4,
            "material_index": 2,
            "material": "No Edge Banding",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 11159.782,
            "center_local_mm": {
              "x": -0.0,
              "y": -0.0,
              "z": -93.508
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1570.605,
              "z": 746.914
            },
            "normal_local": {
              "x": -0.0,
              "y": 0.0,
              "z": -1.0
            },
            "normal_world": {
              "x": -0.0,
              "y": 0.0,
              "z": -1.0
            },
            "face_signature": "z-@-0.0,-0.0,-93.508",
            "vertices_local_mm": [
              {
                "x": 372.0,
                "y": 7.5,
                "z": -93.508
              },
              {
                "x": 372.0,
                "y": -7.5,
                "z": -93.508
              },
              {
                "x": -372.001,
                "y": -7.5,
                "z": -93.508
              },
              {
                "x": -372.001,
                "y": 7.5,
                "z": -93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.005,
                "y": -1563.105,
                "z": 746.914
              },
              {
                "x": 2664.005,
                "y": -1578.105,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1578.105,
                "z": 746.914
              },
              {
                "x": 1920.004,
                "y": -1563.106,
                "z": 746.914
              }
            ]
          },
          {
            "polygon_index": 5,
            "material_index": 1,
            "material": "Edge Banding (Com fita)",
            "loop_total": 4,
            "vertex_count": 4,
            "area_mm2": 11159.784,
            "center_local_mm": {
              "x": 0.0,
              "y": 0.0,
              "z": 93.508
            },
            "center_world_mm": {
              "x": 2292.004,
              "y": -1570.605,
              "z": 933.93
            },
            "normal_local": {
              "x": 0.0,
              "y": 0.0,
              "z": 1.0
            },
            "normal_world": {
              "x": 0.0,
              "y": 0.0,
              "z": 1.0
            },
            "face_signature": "z+@0.0,0.0,93.508",
            "vertices_local_mm": [
              {
                "x": 372.001,
                "y": -7.5,
                "z": 93.508
              },
              {
                "x": 372.001,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": -372.0,
                "y": 7.5,
                "z": 93.508
              },
              {
                "x": -372.0,
                "y": -7.5,
                "z": 93.508
              }
            ],
            "vertices_world_mm": [
              {
                "x": 2664.005,
                "y": -1578.105,
                "z": 933.93
              },
              {
                "x": 2664.005,
                "y": -1563.105,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1563.106,
                "z": 933.93
              },
              {
                "x": 1920.004,
                "y": -1578.105,
                "z": 933.93
              }
            ]
          }
        ]
      },
      "custom_props": {
        "notes": "Fachada Armário - Tampo Lateral.001"
      }
    }
  ]
}
'''


def round3(v):
    return round(float(v), 3)


def get_scene_scale_length():
    us = bpy.context.scene.unit_settings
    return us.scale_length if us.scale_length else 1.0


def mm_to_scene_units(mm):
    # No seu arquivo atual scale_length=0.001 => 1 BU = 1 mm
    # Fórmula genérica:
    # mm / (1000 * scale_length)
    return mm / (1000.0 * get_scene_scale_length())


def vec_mm_to_scene(d):
    return Vector((
        mm_to_scene_units(d["x"]),
        mm_to_scene_units(d["y"]),
        mm_to_scene_units(d["z"]),
    ))


def ensure_material(name):
    mat = bpy.data.materials.get(name)
    if mat is None:
        mat = bpy.data.materials.new(name=name)
    return mat


def clear_materials(obj):
    obj.data.materials.clear()


def vec_to_sig(v):
    return f"{round3(v.x)},{round3(v.y)},{round3(v.z)}"


def get_face_signature_from_normal_and_center(normal, center):
    n = normal.normalized()
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

    return f"{dominant_axis}{sign}@{vec_to_sig(center)}"


def get_mesh_face_signatures(obj):
    mesh = obj.data
    result = {}

    for poly in mesh.polygons:
        sig = get_face_signature_from_normal_and_center(poly.normal, poly.center)
        result[sig] = poly.index

    return result


def build_material_slot_map(obj, material_names):
    clear_materials(obj)
    slot_map = {}

    for mat_name in material_names:
        if mat_name in slot_map:
            continue

        mat = ensure_material(mat_name)
        obj.data.materials.append(mat)
        slot_map[mat_name] = len(obj.data.materials) - 1

    return slot_map


def assign_materials_from_export(obj, exported_obj):
    slot_map = build_material_slot_map(obj, exported_obj["materials"])
    mesh = obj.data

    recreated_face_sig_to_poly = get_mesh_face_signatures(obj)

    for face in exported_obj["material_assignments"]["faces"]:
        exported_sig = face["face_signature"]
        material_name = face["material"]

        poly_index = recreated_face_sig_to_poly.get(exported_sig)
        if poly_index is None:
            print(f"[WARN] Face signature não encontrada em {obj.name}: {exported_sig}")
            continue

        if material_name not in slot_map:
            print(f"[WARN] Material não encontrado no slot_map de {obj.name}: {material_name}")
            continue

        mesh.polygons[poly_index].material_index = slot_map[material_name]

    mesh.update()


def create_box_mesh_object(name, dims_mm, location_scene, collection):
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)

    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=2.0)
    bm.to_mesh(mesh)
    bm.free()

    obj.location = location_scene
    obj.rotation_euler = (0.0, 0.0, 0.0)

    sx = mm_to_scene_units(dims_mm["x"]) / 2.0
    sy = mm_to_scene_units(dims_mm["y"]) / 2.0
    sz = mm_to_scene_units(dims_mm["z"]) / 2.0
    obj.scale = (sx, sy, sz)

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.select_set(False)

    return obj


def compute_group_center_scene(exported_objects):
    mins = Vector((float("inf"), float("inf"), float("inf")))
    maxs = Vector((float("-inf"), float("-inf"), float("-inf")))

    for item in exported_objects:
        loc = vec_mm_to_scene(item["location_mm"])
        dims = Vector((
            mm_to_scene_units(item["dimensions_mm"]["x"]),
            mm_to_scene_units(item["dimensions_mm"]["y"]),
            mm_to_scene_units(item["dimensions_mm"]["z"]),
        ))
        half = dims / 2.0
        obj_min = loc - half
        obj_max = loc + half

        mins.x = min(mins.x, obj_min.x)
        mins.y = min(mins.y, obj_min.y)
        mins.z = min(mins.z, obj_min.z)

        maxs.x = max(maxs.x, obj_max.x)
        maxs.y = max(maxs.y, obj_max.y)
        maxs.z = max(maxs.z, obj_max.z)

    return (mins + maxs) / 2.0


def ensure_collection(name):
    coll = bpy.data.collections.get(name)
    if coll is None:
        coll = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(coll)
    return coll


def recreate_from_export(data):
    exported_objects = data["objects"]
    cursor_loc = bpy.context.scene.cursor.location.copy()

    original_group_center = compute_group_center_scene(exported_objects)
    translation = cursor_loc - original_group_center

    collection = ensure_collection("Recreated From Export")

    created = []

    for item in exported_objects:
        loc_scene = vec_mm_to_scene(item["location_mm"]) + translation

        obj = create_box_mesh_object(
            name=item["name"],
            dims_mm=item["dimensions_mm"],
            location_scene=loc_scene,
            collection=collection
        )

        assign_materials_from_export(obj, item)

        for k, v in item.get("custom_props", {}).items():
            obj[k] = v

        created.append(obj)

    bpy.ops.object.select_all(action='DESELECT')
    for obj in created:
        obj.select_set(True)

    if created:
        bpy.context.view_layer.objects.active = created[0]

    print(f"[OK] {len(created)} objetos recriados.")
    print("[OK] Centro do grupo alinhado ao cursor 3D.")


def main():
    data = json.loads(DATA_JSON)

    expected = data.get("meta", {}).get("selected_count")
    actual = len(data.get("objects", []))

    print(f"[INFO] selected_count no JSON: {expected}")
    print(f"[INFO] objects no JSON: {actual}")

    if expected is not None and expected != actual:
        print("[WARN] selected_count difere da quantidade real de objetos no JSON.")

    recreate_from_export(data)


main()
