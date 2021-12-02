
from utils.all_components_list import get_all_components


class Edit_entity_menu_state:
	def __init__(self):
		self.__cursor = 0
		self.__menu_mods = ['CHOOSING_MAIN_OPTION', 'CHOOSING_COMPONENT', 'EDIT_COMPONENT']
		self.__edit_menu_options = ['Add component', 'Delete component', 'Edit component']
		self.mode = 0
		self.edit_chosen_option = 0
		self.__all_components = get_all_components()

	def up_cursor(self):
		self.__cursor -= 1

	def down_cursor(self):
		self.__cursor += 1

	def zero_cursor(self):
		self.__cursor = 0
	
	def up_mode(self):
		self.mode += 1
		print('\nCurrent menu mode: %s'%(self.__menu_mods[self.mode]))

	def down_mode(self):
		self.mode -= 1
		print('\nCurrent menu mode: %s'%(self.__menu_mods[self.mode]))

	def zero_mode(self):
		self.mode = 0
		print('\nCurrent menu mode: %s'%(self.__menu_mods[self.mode]))

	def zero_state(self):
		self.zero_cursor()
		self.zero_mode()
		self.edit_chosen_option = 0

	@property
	def cursor(self):
		return self.__cursor

	@property
	def edit_menu_options(self):
		return self.__edit_menu_options

	@property
	def all_components(self):
		return self.__all_components