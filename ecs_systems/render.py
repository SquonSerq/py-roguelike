from bearlibterminal import terminal as blt

from utils.blt_configurator import Blt_configurator

class Render_system:
	def __init__(self, ctx, ctrls):
		self.__context = ctx
		self.__controls = ctrls
		self.__name = 'render_system'
		self.__blt_configurator = Blt_configurator()

		self.__blt_configurator.set_window_size(50, 50)
		self.__blt_configurator.set_cellsize(width=15, height=15)
		

	def update(self):
		for i in range(0, 50):
			for j in range(0, 50):
				blt.put(j, i, '.')

		for entity in self.__context.entity_manager.entities:
			if entity.contains('transform_component') and entity.contains('texture_component'):

				if entity.contains('layer_component'):
					blt.layer(entity.get_component('layer_component').layer)

				transform = entity.get_component('transform_component')
				texture = entity.get_component('texture_component')
				blt.clear_area(transform.x, transform.y, 1, 1)
				blt.put(transform.x, transform.y, texture.texture)

				blt.layer(0)

	@property
	def name(self):
		return self.__name
