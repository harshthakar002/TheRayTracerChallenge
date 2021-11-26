from math import pi
from features.color import Color
from features.point import Point
from features.vector import Vector
from figures.plane import Plane
from figures.sphere import Sphere
from physical.point_light import PointLight
from physical.world import World
from physical.camera import Camera
from transformations.view_transformer import ViewTransformer
from physical.renderer import Renderer
from canvas.ppm_writer import PPMWriter

floor = Plane()
floor.material.color = Color(1, 0.9, 0.9)
floor.material.specular = 1

left_wall = Plane()
left_wall.translation(0, 0, 5).rotation_y(-pi / 4).rotation_x(pi / 2)
left_wall.material = floor.material

right_wall = Plane()
right_wall.translation(0, 0, 5).rotation_y(pi / 4).rotation_x(pi / 2)
right_wall.material = floor.material

middle = Sphere()
middle.translation(-0.5, 1, 0.5)
middle.material.color = Color(0, 0, 1)
middle.material.diffuse = 1
middle.material.specular = 1

right = Sphere()
right.translation(1.5, 0.5, -0.5).scaling(0.5, 0.5, 0.5)
right.material.color = Color(0.0, 1, 0.0)
right.material.diffuse = 1
right.material.specular = 1

left = Sphere()
left.translation(-1.5, 0.33, -0.75).scaling(0.33, 0.33, 0.33)
left.material.color = Color(1, 0, 0)
left.material.diffuse = 1
left.material.specular = 1

light = PointLight(Color(1, 1, 1), Point(-10, 10, -10))
world = World()
world.objects = [floor, left_wall, right_wall, middle, left, right]
world.light = light

transform = ViewTransformer.view_transform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))
camera = Camera(250, 125, pi / 3, transform)
canvas = Renderer.render(camera, world)

ppm = PPMWriter.write_ppm_from_canvas(canvas)
with open('out/plane_basic.ppm', 'w') as f:
    f.write('\n'.join(ppm))