from bearlibterminal import terminal as blt

class Controls:
	def __init__(self):
		self.__pressed_buttons = []

	def check(self):
		self.__pressed_buttons.clear()

		while blt.has_input():
			self.__pressed_buttons.append(blt.read())

	@property
	def get_input(self):
		if len(self.__pressed_buttons) > 0:
			return self.__pressed_buttons[0]
