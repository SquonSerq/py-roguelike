import os, sys

dir_path = os.path.realpath('./components/')
files_in_dir = [f[:-3] for f in os.listdir(dir_path)
                if f.endswith('.py') and f != '__init__.py' and f != 'all_components_list.py']
for f in files_in_dir:
    mod = __import__('.'.join(['components', f]), fromlist=[f])
    to_import = [getattr(mod, x) for x in dir(mod)
                if isinstance(getattr(mod, x), type)]  # if you need classes only

    for i in to_import:
        try:
            setattr(sys.modules[__name__], i.__name__, i)
        except AttributeError:
            pass

def get_all_components():
	l = os.listdir('./components')
	li = [x.split('.')[0] for x in l if x != '__pycache__']
	return li

def create_component_by_name(name, **kwargs):
	component_name = name.capitalize()
	component_class = globals()[component_name]
	return component_class(**kwargs)