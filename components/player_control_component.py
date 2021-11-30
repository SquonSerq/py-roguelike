class Player_control_component:
	def __init__(self, **buttons):
		self.name = 'player_control_component'
		self.up = buttons['up']
		self.down = buttons['down']
		self.left = buttons['left']
		self.right = buttons['right']