bl_info = {
    "name": "Isolate Light",
    "blender": (2, 80, 0),
    "category": "Lighting",
    "description": "Toggles light isolation",
    "author": "Bubu",
    "version": (0, 1, 0),
}

import bpy

class IsolateLight(bpy.types.Operator):
    """Isolates a selected light"""
    bl_idname = "object.isolate_light"
    bl_label = "Isolate Light"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        
        # The original script
        visible = True
        for i in bpy.context.scene.objects:
            if i.hide_viewport == True:
                visible = False
                break
        if visible == True:
            for i in bpy.context.scene.objects:
                if i.type == 'LIGHT' and i != bpy.context.object:
                    i.hide_viewport = True
        else:
            for i in bpy.context.scene.objects:
                if i.type == 'LIGHT':
                    i.hide_viewport = False

        return {'FINISHED'}

    def draw(self, context):
        self.layout.operator("object.isolate_light")

def menu_func(self, context):
    self.layout.operator(IsolateLight.bl_idname)

def register():
    bpy.utils.register_class(IsolateLight)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(IsolateLight)

if __name__ == "__main__":
    register()