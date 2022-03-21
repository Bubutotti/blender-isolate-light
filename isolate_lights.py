bl_info = {
    "name": "Isolate Lights",
    "blender": (2, 80, 0),
    "category": "Lighting",
    "description": "Toggles unselected lights visibility",
    "author": "Bubu",
    "version": (0, 2, 1),
}

import bpy

class IsolateLights(bpy.types.Operator):
    """Isolates selected lights"""
    bl_idname = "object.isolate_lights"
    bl_label = "Isolate Lights"
    bl_options = {'REGISTER', 'UNDO'}
    
    selection = []
    def execute(self, context):
        selection = self.selection
        if selection == []: # Nothing is hidden
            lights = [x for x in context.scene.objects if x.type == 'LIGHT']
            for obj in lights:
                if not obj in context.selected_objects and not obj.hide_viewport:
                    selection.append(obj)
            for obj in selection:
                obj.hide_viewport = True
        else:
            for obj in selection:
                obj.hide_viewport = False
            selection.clear()
        
        return {'FINISHED'}

    def draw(self, context):
        self.layout.operator("object.isolate_lights")

def menu_func(self, context):
    self.layout.operator(IsolateLights.bl_idname)

def register():
    bpy.utils.register_class(IsolateLights)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(IsolateLights)

if __name__ == "__main__":
    register()
