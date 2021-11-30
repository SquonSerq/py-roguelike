
from utils.entity import Entity


class Entity_manager:
	def __init__(self):
		self.__id_checker = 0
		self.__entities = {}
		self.__tag_entities = {}

	def create_entity(self, **kwargs):
		self.__id_checker += 1
		self.__entities[self.__id_checker] = Entity(self.__id_checker)
		
		if 'tags' in kwargs:
			for tag in kwargs['tags']:
				if tag in self.__tag_entities:
					print('Added entity %i to tag %s'%(self.__id_checker, tag))
					self.__tag_entities[tag].append(self.__entities[self.__id_checker])
				else:
					print('Created tag %s'%(tag))
					print('Added entity %i to tag %s'%(self.__id_checker, tag))
					self.__tag_entities[tag] = []
					self.__tag_entities[tag].append(self.__entities[self.__id_checker])

		return self.__entities[self.__id_checker]

	def delete_entity(self, id):
		if id in self.__entities:
			self.__entities.pop(id)

	def clear(self):
		self.__entities.clear()

	def delete_entity_from_tag(self, id, tag):
		if id in self.__entities and tag in self.__tag_entities:
			if self.__entities[id] in self.__tag_entities[tag]:
				self.__tag_entities.get(tag).pop(self.__entities[id])

	@property
	def entities(self):
		return self.__entities.values()