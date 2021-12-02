from bearlibterminal import terminal as blt
from components.movement_component import Movement_component
from components.player_control_component import Player_control_component
from components.texture_component import Texture_component

from components.transform_component import Transform_component
from ecs_systems.player_control import Player_control_system
from ecs_systems.render import Render_system
from utils.config_reader import Config_reader, get_keycode
from utils.editor.components.cursor_component import Cursor_component
from utils.editor.systems.cursor_movement import Cursor_movement
from utils.editor.systems.cursor_place import Cursor_place

class Editor_scene:
	def __init__(self, scene_manager):
		self.__scene_manager = scene_manager
		self.__config_reader = Config_reader()
		self.__keybard_shortcuts = self.__config_reader.get_from_file('keyboard')

	def on_instance(self, ctx, ctrls):
		if not ctx.entity_manager.get_entities_by_tag('cursor'):
			cursor = ctx.entity_manager.create_entity(tags=['cursor'])
			cursor.add_component(Transform_component(1, 1))
			cursor.add_component(Texture_component('X'))
			cursor.add_component(Movement_component())
			cursor.add_component(Player_control_component(up=get_keycode(self.__keybard_shortcuts['move_up']), down=get_keycode(self.__keybard_shortcuts['move_down']), left=get_keycode(self.__keybard_shortcuts['move_left']), right=get_keycode(self.__keybard_shortcuts['move_right'])))
			cursor.add_component(Cursor_component())


		ctx.system_manager.add_system(Cursor_place(ctx, ctrls, self.__scene_manager))
		ctx.system_manager.add_system(Player_control_system(ctx, ctrls))
		ctx.system_manager.add_system(Cursor_movement(ctx, ctrls))
		ctx.system_manager.add_system(Render_system(ctx, ctrls))

	def update(self, **kwargs):
		ctx = kwargs["context"]
		ctrls = kwargs["controls"]

		if ctrls.get_input == blt.TK_ENTER:
			self.__scene_manager.set_scene('edit_entity')

		ctx.system_manager.update()