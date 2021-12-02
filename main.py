from bearlibterminal import terminal as blt
from controls import Controls
from utils.blt_configurator import Blt_configurator
from utils.config_reader import Config_reader
from utils.context import Context
from utils.scene_init import scene_init
from utils.scene_manager import Scene_manager

if __name__ == "__main__":
	blt.open()
	blt.refresh()
	
	blt_configurator = Blt_configurator()

	blt_configurator.set("window.title='py-roguelike'; window.cellsize=auto; window.fullscreen=false")

	controls = Controls()
	ctx = Context()
	scene_manager = Scene_manager(ctx, controls)

	scene_init(scene_manager)

	scene_manager.set_scene('main_menu')

	while True:
		blt.clear()

		controls.check()

		scene_manager.update()

		blt.refresh()
		if controls.get_input == blt.TK_CLOSE:
			blt.close()
			break

