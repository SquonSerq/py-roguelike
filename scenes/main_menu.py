from bearlibterminal import terminal as blt

class Main_menu:
	def __init__(self, scene_manager):
		self.__scene_manager = scene_manager

	def on_instance(self, ctx, ctrls):
		ctx = ctx
		self.cursor = 0


	def update(self, **kwargs):
		ctx = kwargs["context"]
		ctrls = kwargs["controls"]


		if ctrls.get_input == blt.TK_W:
			if self.cursor > 0:
				self.cursor -= 1
		elif ctrls.get_input == blt.TK_S:
			if self.cursor < 8:
				self.cursor += 1

		if ctrls.get_input == blt.TK_ENTER:
			if self.cursor == 0:
				self.__scene_manager.set_scene('test_scene')

		blt.put(4, 7+self.cursor, ">")

		blt.printf(5, 5, "Main menu")	

		blt.printf(5, 7, "Start game")
		blt.printf(5, 8, "Editor")

		ctx.system_manager.update()