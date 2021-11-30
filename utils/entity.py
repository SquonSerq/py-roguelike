

class Entity:
	def __init__(self):
		self.__components = {}

	def addComponent(self, component):
		self.__components[component.name] = component

	def contains(self, component_name):
		if component_name in self.__components:
			return True
		else:
			return False

	def get_component(self, component_name):
		if self.__components[component_name]:
			return self.__components[component_name]
