
class System_manager:
	def __init__(self):
		self.__systems = {}
		
	def update(self):
		for system in self.__systems.values():
			system.update()
	
	def add_system(self, system):
		self.__systems[system.name] = system

	def clear(self):
		self.__systems.clear()