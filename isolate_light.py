bl_info = {
    "name": "Isolate Light",
    "blender": (2, 80, 0),
    "category": "Lighting",
    "description": "Toggles unselected lights visibility",
    "author": "Bubu",
    "version": (0, 2, 0),
}

import bpy

class IsolateLight(bpy.types.Operator):
    """Isolates a selected light"""
    bl_idname = "object.isolate_light"
    bl_label = "Isolate Light"
    bl_options = {'REGISTER', 'UNDO'}
    
    selection = []
    def execute(self, context):
        if self.selection == []: # Nothing is hidden
            for object in context.scene.objects:
                if object.type == 'LIGHT':
                    self.selection.append(object)
            for object in context.selected_objects:
                if object.type == 'LIGHT':
                    self.selection.remove(object)
            for object in self.selection:
                if object.hide_viewport == True: # Prevents conflict with manually hidden objects
                    self.selection.remove(object)
            for object in self.selection:
                object.hide_viewport = True
        else:
            for object in self.selection:
                object.hide_viewport = False
            self.selection.clear()
        
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
