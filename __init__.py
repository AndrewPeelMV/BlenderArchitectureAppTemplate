import bpy

from . import object_properties_panel
from . import remove_blender_ui
from . import room_designer

def register():
	object_properties_panel.register()
	remove_blender_ui.register()
	room_designer.register()