class Movement_system:
	def __init__(self, ctx, ctrls):
		self.__context = ctx
		self.__controls = ctrls
		self.__name = 'movement_system'

	def update(self):
		for entity in self.__context.entity_manager.entities:
			if entity.contains('movement_component') and entity.contains('transform_component'):
				mc = entity.get_component('movement_component')
				tc = entity.get_component('transform_component')

				if ((mc.x != 0 or mc.y !=0)
				and tc.x + mc.x < 80 and tc.x + mc.x >= 0
				and tc.y + mc.y < 25 and tc.y + mc.y >= 0):

					# check if there are any obstacles on the way
					for obstacle in self.__context.entity_manager.get_entities_by_tag('collision'):
						if obstacle.contains('transform_component'):
							
							if obstacle.id == entity.id:
								continue

							otc = obstacle.get_component('transform_component')
							
							if (tc.x+mc.x == otc.x and tc.y+mc.y == otc.y):
								mc.x = mc.y = 0
								break

					tc.x += mc.x
					tc.y += mc.y

				mc.x = mc.y = 0

	@property
	def name(self):
		return self.__name
