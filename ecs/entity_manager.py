from ecs.entity import Entity

class Entity_manager:
	def __init__(self):
		self.__id_checker = 0
		self.__entities = {}
		self.__tag_entities = {}

	def create_entity(self, **kwargs):
		self.__id_checker += 1
		self.__entities[self.__id_checker] = Entity(self.__id_checker)
		print('\nCreated entity with id: %i'%(self.__id_checker))
		
		if 'tags' in kwargs:
			for tag in kwargs['tags']:
				self.add_entity_to_tag(self.__entities[self.__id_checker], tag)

		return self.__entities[self.__id_checker]

	def delete_entity(self, id):
		if id in self.__entities:
			self.__entities.pop(id)

	def clear(self):
		self.__tag_entities.clear()
		self.__entities.clear()
		self.__id_checker = 0

	def delete_entity_from_tag(self, entity, tag):
		if tag in self.__tag_entities:
			if entity in self.__tag_entities['tag']:
				self.__tag_entities[tag].pop(entity)

	def get_entities_by_tag(self, tag):
		if tag in self.__tag_entities:
			return self.__tag_entities[tag]

	def add_entity_to_tag(self, entity, tag):
		if tag in self.__tag_entities:
			print('Added entity %i to tag %s'%(entity.id, tag))
			self.__tag_entities[tag].append(entity)
		else:
			print('Created tag %s'%(tag))
			print('Added entity %i to tag %s'%(entity.id, tag))
			self.__tag_entities[tag] = []
			self.__tag_entities[tag].append(entity)

	def delete_tag(self, tag):
		print("Deleted tag: %s"%(tag))
		self.__tag_entities.pop(tag, None)


	@property
	def entities(self):
		return self.__entities.values()