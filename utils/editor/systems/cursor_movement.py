class Cursor_movement:
	def __init__(self, ctx, ctrls):
		self.__context = ctx
		self.__controls = ctrls
		self.__name = 'cursor_movement'

	def update(self):
		for cursor in self.__context.entity_manager.get_entities_by_tag('cursor'):
			if cursor.contains('cursor_component') and cursor.contains('transform_component') and cursor.contains('movement_component'):
				ct = cursor.get_component('transform_component')
				cm = cursor.get_component('movement_component')

				if cm.x != 0 or cm.y != 0:
					ct.x += cm.x
					ct.y += cm.y

				cm.x = cm.y = 0


	@property
	def name(self):
		return self.__name
