
from utils.entity import Entity


class Entity_manager:
	def __init__(self):
		self.__id_checker = 0
		self.__entities = {}

	def createEntity(self):
		self.__id_checker += 1
		self.__entities[self.__id_checker] = Entity()
		return self.__entities[self.__id_checker]

	def deleteEntity(self, id):
		self.__entities.pop(id)

	def clear(self):
		self.__entities.clear()

	@property
	def entities(self):
		return self.__entities.values()