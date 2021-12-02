from bearlibterminal import terminal as blt
from utils.all_components_list import create_component_by_name, get_all_components

from utils.blt_configurator import Blt_configurator
from utils.editor.editor_utils.edit_entity_menu_state import Edit_entity_menu_state

class Edit_entity:
	def __init__(self, scene_manager):
		self.__scene_manager = scene_manager
		self.start_option_height = 5
		self.__menu_state = Edit_entity_menu_state()

	def on_instance(self, ctx, ctrls):
		ctx.system_manager.clear()
		Blt_configurator().set_window_size(80, 25)

		self.entity = ctx.entity_manager.get_entities_by_tag('edit_entity')[0]

	def update(self, **kwargs):
		ctx = kwargs["context"]
		ctrls = kwargs["controls"]


		if ctrls.get_input == blt.TK_W:
			self.__menu_state.up_cursor()
		elif ctrls.get_input == blt.TK_S:
			self.__menu_state.down_cursor()

		if ctrls.get_input == blt.TK_ESCAPE:
			if self.__menu_state.mode == 0:
				self.__scene_manager.set_scene('editor_main')
			elif self.__menu_state.mode > 0:
				self.__menu_state.down_mode()

		if ctrls.get_input == blt.TK_ENTER:
			if self.__menu_state.mode == 0:
				self.__menu_state.up_mode()
				self.__menu_state.edit_chosen_option = self.__menu_state.cursor
				self.__menu_state.zero_cursor()
			elif self.__menu_state.mode == 1:
				if self.__menu_state.edit_chosen_option == 0:
					self.entity.add_component(create_component_by_name(get_all_components()[self.__menu_state.cursor]))
					self.__menu_state.zero_state()
				elif self.__menu_state.edit_chosen_option == 1:
					# TODO: refactor. get rid of for
					for i, component in  enumerate(self.entity.all_components):
						if i == self.__menu_state.cursor:
							self.entity.delete_component(component.name)
							self.__menu_state.zero_state()
							break

		# RENDERING
		# lines
		for i in range(0, 25):
			blt.put(3, i, '|')
			blt.put(30, i, '|')

		# renders elements depending on menu state mode
		if self.__menu_state.mode == 0:
			blt.put(4, 5+self.__menu_state.cursor, '>')
		elif self.__menu_state.mode == 1:
			blt.put(31, 5+self.__menu_state.cursor, '>')

			if self.__menu_state.edit_chosen_option == 0:
				i = 0
				for component in self.__menu_state.all_components:
					blt.print(32, self.start_option_height+i, component)
					i += 1
			elif self.__menu_state.edit_chosen_option == 1:
				i = 0
				for component in self.entity.all_components:
					blt.print(32, self.start_option_height+i, component.name)
					i+=1
			elif self.__menu_state.edit_chosen_option == 2:
				i = 0
				for component in self.entity.all_components:
					blt.print(32, self.start_option_height+i, component.name)
					i+=1


		option_height = 5
		for option in self.__menu_state.edit_menu_options:
			blt.printf(5, option_height, option)
			option_height += 1

		ctx.system_manager.update()