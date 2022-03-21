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
    bl_options = {"REGISTER", "UNDO"}

    selection = {}

    def execute(self, context):
        if not self.selection:
            all_lights = set(filter(lambda x: x.type == "LIGHT", context.scene.objects))
            selected_lights = set(filter(lambda x: x.type == "LIGHT", context.selected_objects))
            hidden_lights = set(filter(lambda x: x.hide_viewport == True, context.scene.objects))
            
            IsolateLights.selection = selected_lights ^ all_lights ^ hidden_lights
            
            for i in self.selection:
                i.hide_viewport = True
        else:
            for i in self.selection:
                i.hide_viewport = False
            IsolateLights.selection = {}

        return {"FINISHED"}


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
