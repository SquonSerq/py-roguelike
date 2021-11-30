import json
from components.movement_component import Movement_component
from components.player_control_component import Player_control_component
from components.texture_component import Texture_component
from components.transform_component import Transform_component

from bearlibterminal import terminal as blt

from components.wall_component import Wall_component

class Lever_reader:
	def __init__(self, map_path, ctx):
		self.__map_path = map_path
		self.__ctx = ctx

	def process_map(self):
		with open(self.__map_path) as json_file:
			data = json.load(json_file)

			for entity in data.values():
				if "tags" in entity:
					ent = self.__ctx.entity_manager.create_entity(tags=entity['tags'])
				else:
					ent = self.__ctx.entity_manager.create_entity()


				for component in entity['components']:
					if 'transform_component' in component.keys():
						ent.add_component(Transform_component(component['transform_component']['x'], component['transform_component']['y']))
					elif 'texture_component' in component.keys():
						ent.add_component(Texture_component(component['texture_component']['texture']))
					elif 'movement_component' in component.keys():
						ent.add_component(Movement_component())
					elif 'player_control_component' in component.keys():
						ent.add_component(Player_control_component(up=blt.TK_W, down=blt.TK_S, left=blt.TK_A, right=blt.TK_D))
					elif 'wall_component' in component.keys():
						ent.add_component(Wall_component())
					

