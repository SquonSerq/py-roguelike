from components.movement_component import Movement_component
from components.player_control_component import Player_control_component
from components.texture_component import Texture_component
from components.transform_component import Transform_component
from ecs_systems.movement import Movement_system
from ecs_systems.player_control import Player_control_system
from ecs_systems.render import Render_system

from bearlibterminal import terminal as blt

class Test_scene:
	def on_instance(self, ctx, ctrls):
		player = ctx.entity_manager.createEntity()
		player.addComponent(Transform_component(1, 1))
		player.addComponent(Texture_component('@'))
		player.addComponent(Movement_component())
		player.addComponent(Player_control_component(up=blt.TK_W, down=blt.TK_S, left=blt.TK_A, right=blt.TK_D))

		# test entity to check if game drops with empty entity
		dropEnt = ctx.entity_manager.createEntity()

		ctx.system_manager.addSystem(Player_control_system(ctx, ctrls))
		ctx.system_manager.addSystem(Movement_system(ctx, ctrls))
		ctx.system_manager.addSystem(Render_system(ctx, ctrls))

	def update(self, **kwargs):
		ctx = kwargs["context"]
		ctrls = kwargs["controls"]
		ctx.system_manager.update()
