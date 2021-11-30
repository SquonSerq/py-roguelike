class Player_control_system:
	def __init__(self, ctx, ctrls):
		self.__context = ctx
		self.__controls = ctrls
		self.__name = 'player_control_system'

	def update(self):
		for entity in self.__context.entity_manager.entities:
			if (entity.contains('player_control_component')
			and entity.contains('movement_component')
			and entity.contains('transform_component')):
				pc = entity.get_component('player_control_component')
				mc = entity.get_component('movement_component')

				pressed_button = self.__controls.get_input

				if pressed_button == pc.up:
					mc.y -= 1
				elif pressed_button == pc.down:
					mc.y += 1
				elif pressed_button == pc.left:
					mc.x -= 1
				elif pressed_button == pc.right:
					mc.x += 1


	@property
	def name(self):
		return self.__name