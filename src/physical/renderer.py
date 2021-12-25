from physical.camera import Camera
from physical.world import World
from canvas.canvas import Canvas
from physical.shader import Shader
from figures.ray import Ray
from datetime import datetime

class Renderer():

    @staticmethod
    def render(camera: Camera, world: World, depth: int = 1) -> Canvas:
        image = Canvas(camera.hsize, camera.vsize)
        for y in range(camera.vsize):
            start = datetime.now()
            for x in range(camera.hsize):
                ray = Ray.ray_for_pixel(camera, x, y)
                color = Shader.color_at(world, ray, depth)
                image.write_pixel(x, y, color)
            print(str(y) + ': ' + str(datetime.now() - start))
        return image