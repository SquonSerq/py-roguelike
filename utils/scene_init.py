from scenes.main_menu import Main_menu
from scenes.test_scene import Test_scene
from utils.editor.scenes.edit_entity import Edit_entity
from utils.editor.scenes.editor_scene import Editor_scene


def scene_init(scene_manager):
	scene_manager.add_scene('test_scene', Test_scene(scene_manager))
	scene_manager.add_scene('main_menu', Main_menu(scene_manager))

	# editor scenes
	scene_manager.add_scene('editor_main', Editor_scene(scene_manager))
	scene_manager.add_scene('edit_entity', Edit_entity(scene_manager))
