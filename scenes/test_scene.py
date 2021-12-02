from components.movement_component import Movement_component
from components.player_control_component import Player_control_component
from components.texture_component import Texture_component
from components.transform_component import Transform_component
from components.wall_component import Wall_component
from ecs_systems.movement import Movement_system
from ecs_systems.player_control import Player_control_system
from ecs_systems.render import Render_system

from bearlibterminal import terminal as blt
from utils.config_reader import Config_reader, get_keycode

from utils.level_reader import Lever_reader

class Test_scene:
	def __init__(self, scene_manager):
		self.__scene_manager = scene_manager
		self.__config_reader = Config_reader()
		self.__keybard_shortcuts = self.__config_reader.get_from_file('keyboard')

	def on_instance(self, ctx, ctrls):
		ctx.entity_manager.clear()
		ctx.system_manager.clear()

		reader = Lever_reader('./maps/map_test.json', ctx)
		reader.process_map()

		player = ctx.entity_manager.create_entity(tags=['player', 'collision', 'movable'])
		player.add_component(Transform_component(1, 1))
		player.add_component(Texture_component('@'))
		player.add_component(Movement_component())
		player.add_component(Player_control_component(up=get_keycode(self.__keybard_shortcuts['move_up']), down=get_keycode(self.__keybard_shortcuts['move_down']), left=get_keycode(self.__keybard_shortcuts['move_left']), right=get_keycode(self.__keybard_shortcuts['move_right'])))

		wall = ctx.entity_manager.create_entity(tags=['walls', 'collision'])
		wall.add_component(Transform_component(5, 5))
		wall.add_component(Texture_component('#'))
		wall.add_component(Wall_component())

		# test entity to check if game drops with empty entity
		dropEnt = ctx.entity_manager.create_entity()

		ctx.system_manager.add_system(Player_control_system(ctx, ctrls))
		ctx.system_manager.add_system(Movement_system(ctx, ctrls))
		ctx.system_manager.add_system(Render_system(ctx, ctrls))

	def update(self, **kwargs):
		ctx = kwargs["context"]
		ctrls = kwargs["controls"]

		if ctrls.get_input == blt.TK_ESCAPE:
			self.__scene_manager.set_scene('main_menu')

		ctx.system_manager.update()
