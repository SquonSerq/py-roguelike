from utils.entity_manager import Entity_manager
from utils.system_manager import System_manager

class Context:
	def __init__(self):
		self.__system_manager = System_manager()
		self.__entity_manager = Entity_manager()

	def update(self):
		self.__system_manager.update(self.__entity_manager.entities)

	@property
	def system_manager(self):
		return self.__system_manager

	@property
	def entity_manager(self):
		return self.__entity_manager