from bearlibterminal import terminal as blt

class Render_system:
	def __init__(self, ctx, ctrls):
		self.__context = ctx
		self.__controls = ctrls
		self.__name = 'render_system'

	def update(self):
		for entity in self.__context.entity_manager.entities:
			if entity.contains('transform_component') and entity.contains('texture_component'):
				transform = entity.get_component('transform_component')
				texture = entity.get_component('texture_component')
				blt.put(transform.x, transform.y, texture.texture)

	@property
	def name(self):
		return self.__name
