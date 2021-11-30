from bearlibterminal import terminal as blt

class Edit_entity:
	def __init__(self, scene_manager):
		self.__scene_manager = scene_manager

	def on_instance(self, ctx, ctrls):
		ctx.system_manager.clear()
		blt.set("window.size=80x25")
		self.start_option_height = 5
		self.cursor = 0
		self.choosen_cursor = 0
		self.cursor_state = 0
		self.edit_options = ['Add component', 'Delete component', 'Edit component']
		self.all_components = ['transform_component', 'texture_component', 'movement_component', 'player_control_component', 'wall_component']

		for cursor in ctx.entity_manager.get_entities_by_tag('cursor'):
			ct = cursor.get_component('transform_component')
			for entity in ctx.entity_manager.entities:
				et = entity.get_component('transform_component')

				if cursor.id == entity.id:
					continue

				if ct.x == et.x and ct.y == ct.y:
					self.entity = entity
					break
				

	def update(self, **kwargs):
		ctx = kwargs["context"]
		ctrls = kwargs["controls"]

		# lines
		for i in range(0, 25):
			blt.put(3, i, '|')
			blt.put(30, i, '|')

		if ctrls.get_input == blt.TK_ESCAPE:
			if self.cursor_state > 0:
				self.cursor_state -= 1
				self.cursor = 0
			else:
				self.__scene_manager.set_scene('editor_main')

		if ctrls.get_input == blt.TK_ENTER:
			self.cursor_state += 1
			self.choosen_cursor = self.cursor
			self.cursor = 0

		if ctrls.get_input == blt.TK_W:
			self.cursor -= 1
		elif ctrls.get_input == blt.TK_S:
			self.cursor += 1

		if self.cursor_state == 0:
			blt.put(4, 5+self.cursor, '>')
		elif self.cursor_state == 1:
			blt.put(31, 5+self.cursor, '>')

			if self.choosen_cursor == 0:
				i = 0
				for component in self.all_components:
					blt.print(32, self.start_option_height+i, component)
					i += 1
			elif self.choosen_cursor == 1:
				i = 0
				for component in self.entity.all_components:
					blt.print(32, self.start_option_height+i, component.name)
					i+=1
			elif self.choosen_cursor == 2:
				i = 0
				for component in self.entity.all_components:
					blt.print(32, self.start_option_height+i, component.name)
					i+=1


		option_height = 5
		for option in self.edit_options:
			blt.printf(5, option_height, option)
			option_height += 1

		ctx.system_manager.update()