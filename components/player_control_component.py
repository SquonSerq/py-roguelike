from utils.config_reader import Config_reader, get_keycode


class Player_control_component:
	def __init__(self, **buttons):
		self.name = 'player_control_component'

		config_reader = Config_reader().get_from_file('keyboard')

		self.up = buttons.get('up', get_keycode(config_reader['move_up']))
		self.down = buttons.get('down', get_keycode(config_reader['move_down']))
		self.left = buttons.get('left', get_keycode(config_reader['move_left']))
		self.right = buttons.get('right', get_keycode(config_reader['move_right']))