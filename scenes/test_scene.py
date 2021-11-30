from components.texture_component import Texture_component
from components.transform_component import Transform_component
from ecs_systems.render import Render_system

class Test_scene:
	def on_instance(self, ctx, ctrls):
		player = ctx.entity_manager.createEntity()
		player.addComponent(Transform_component(1, 1))
		player.addComponent(Texture_component('@'))

		dropEnt = ctx.entity_manager.createEntity()

		ctx.system_manager.addSystem(Render_system(ctx, ctrls))

	def update(self, **kwargs):
		ctx = kwargs["context"]
		ctrls = kwargs["controls"]
		ctx.system_manager.update()
