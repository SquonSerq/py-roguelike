from bearlibterminal import terminal as blt
from components.texture_component import Texture_component

from components.transform_component import Transform_component

class Cursor_place:
	def __init__(self, ctx, ctrls, scene_manager):
		self.__context = ctx
		self.__controls = ctrls
		self.__scene_manager = scene_manager
		self.__name = 'cursor_place'

	def update(self):
		if self.__controls.get_input == blt.TK_P:
			entityExistsAtPoint = False
			for cursor in self.__context.entity_manager.get_entities_by_tag('cursor'):
				if cursor.contains('cursor_component') and cursor.contains('transform_component'):
					ct = cursor.get_component('transform_component')
					for check_entity in self.__context.entity_manager.entities:

						if check_entity.contains('transform_component'):
							if cursor.id == check_entity.id:
								continue
							cht = check_entity.get_component('transform_component')

							if cht.x == ct.x and cht.y == ct.y:
								entityExistsAtPoint = True
								break
					if entityExistsAtPoint:
						break

					ent = self.__context.entity_manager.create_entity()
					ent.add_component(Transform_component(ct.x, ct.y))
					ent.add_component(Texture_component('?'))

	@property
	def name(self):
		return self.__name