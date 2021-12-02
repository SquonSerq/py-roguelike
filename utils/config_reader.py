import os, json
from bearlibterminal import terminal as blt

def get_keycode(key):
	return getattr(blt, "TK_%s"%(key))

class Config_reader(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Config_reader, cls).__new__(cls)
		return cls.instance
	
	def __init__(self):
		self.__config_files = {}

		config_files = os.listdir('./config/')

		for file in config_files:
			if os.path.isfile("./config/%s"%(file)):
				with open("./config/%s"%(file)) as json_file:
					data = json.load(json_file) 
					self.__config_files[file.replace('.json', '')] = data

	def get_from_file(self, filename):
		return self.__config_files[filename]

	
