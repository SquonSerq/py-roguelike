class Entity:
	def __init__(self, id):
		self.__components = {}
		self.__disabled_components = {}
		self.__id = id

	def add_component(self, component):
		if component.name not in self.__components:
			self.__components[component.name] = component
		else:
			print("Invalid added component: Component %s already exists on Entity %i"%(component.name, self.__id))

	def contains(self, component_name):
		if component_name in self.__components:
			return True
		else:
			return False

	def get_component(self, component_name):
		if component_name in self.__components:
			return self.__components[component_name]

	def delete_component(self, component_name):
		if component_name in self.__components:
			return self.__components.pop(component_name) 

	def disable_component(self, component_name):
		if component_name in self.__components:
			self.__disabled_components[component_name] = self.__components.pop(component_name)

	def enable_component(self, component_name):
		if component_name in self.__disabled_components:
			self.__components[component_name] = self.__disabled_components.pop(component_name)

	@property
	def id(self):
		return self.__id

	@property
	def all_components(self):
		return self.__components.values()
