from physical.camera import Camera
from physical.world import World
from canvas.canvas import Canvas
from physical.shader import Shader
from figures.ray import Ray

class Renderer():

    @staticmethod
    def render(camera: Camera, world: World) -> Canvas:
        image = Canvas(camera.hsize, camera.vsize)
        for y in range(camera.vsize):
            for x in range(camera.hsize):
                ray = Ray.ray_for_pixel(camera, x, y)
                color = Shader.color_at(world, ray, 1)
                image.write_pixel(x, y, color)
        return image