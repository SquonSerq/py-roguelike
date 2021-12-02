from bearlibterminal import terminal as blt

class Blt_configurator(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Blt_configurator, cls).__new__(cls)
		return cls.instance

	def set(self, parameter):
		blt.set(parameter)

	def set_window_size(self, width, height):
		s = "window.size=%ix%i"%(width, height)
		blt.set(s)

	def set_cellsize(self, **kwargs):
		if 'width' and 'height' in kwargs:
			s = "window.cellsize=%ix%i"%(kwargs['width'], kwargs['height'])
		elif 'auto' in kwargs:
			s = "window.cellsize=%s"%(kwargs['auto'])

		blt.set(s)

