from bearlibterminal import terminal as blt
from controls import Controls
from scenes.main_menu import Main_menu
from scenes.test_scene import Test_scene
from utils.context import Context
from utils.editor.scenes.edit_entity import Edit_entity
from utils.editor.scenes.editor_scene import Editor_scene
from utils.scene_manager import Scene_manager

if __name__ == "__main__":
	blt.open()
	blt.refresh()

	blt.set("window.title='py-roguelike'; window.cellsize=auto; window.fullscreen=false")

	controls = Controls()
	ctx = Context()
	scene_manager = Scene_manager(ctx, controls)

	scene_manager.add_scene('test_scene', Test_scene())
	scene_manager.add_scene('main_menu', Main_menu(scene_manager))

	# editor scenes
	scene_manager.add_scene('editor_main', Editor_scene(scene_manager))
	scene_manager.add_scene('edit_entity', Edit_entity(scene_manager))

	scene_manager.set_scene('editor_main')

	while True:
		blt.clear()

		controls.check()

		scene_manager.update()

		blt.refresh()
		if controls.get_input == blt.TK_CLOSE:
			blt.close()
			break

