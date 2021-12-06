class Scene_manager:
	def __init__(self, ctx, ctrls):
		self.__current_scene = ""
		self.__scenes = {}
		self.__context = ctx
		self.__controls = ctrls

	def set_scene(self, scene):
		self.__current_scene = scene
		self.__scenes[self.__current_scene].on_instance(self.__context, self.__controls)

	def add_scene(self, scene_name, scene):
		self.__scenes[scene_name] = scene

	def update(self):
		self.__scenes[self.__current_scene].update(context=self.__context, controls=self.__controls)
