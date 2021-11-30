from bearlibterminal import terminal as blt
from controls import Controls
from scenes.test_scene import Test_scene
from utils.context import Context
from utils.scene_manager import Scene_manager

if __name__ == "__main__":
	blt.open()
	blt.refresh()

	controls = Controls()
	ctx = Context()
	scene_manager = Scene_manager(ctx, controls)

	scene_manager.add_scene('test_scene', Test_scene())

	scene_manager.set_scene('test_scene')

	while True:
		controls.check()

		scene_manager.update()

		blt.refresh()
		if controls.get_input == blt.TK_CLOSE:
			blt.close()
			break

