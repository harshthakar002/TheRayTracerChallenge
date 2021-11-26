from math import pi
from features.color import Color
from features.point import Point
from features.vector import Vector
from figures.sphere import Sphere
from transformations.figure_transformer import FigureTransformer
from physical.point_light import PointLight
from physical.world import World
from physical.camera import Camera
from transformations.view_transformer import ViewTransformer
from physical.renderer import Renderer
from canvas.ppm_writer import PPMWriter

floor = Sphere()
floor.scaling(10, 0.01, 10)
floor.material.color = Color(1, 0.9, 0.9)
floor.material.specular = 0

left_wall = Sphere()
left_wall.translation(0, 0, 5).rotation_y(-pi / 4).rotation_x(pi / 2).scaling(10, 0.01, 10)
left_wall.material = floor.material

right_wall = Sphere()
right_wall.translation(0, 0, 5).rotation_y(pi / 4).rotation_x(pi / 2).scaling(10, 0.01, 10)
right_wall.material = floor.material

middle = Sphere()
middle.translation(-0.5, 1, 0.5)
middle.material.color = Color(0.1, 1, 0.5)
middle.material.diffuse = 0.7
middle.material.specular = 0.3

right = Sphere()
right.translation(1.5, 0.5, -0.5).scaling(0.5, 0.5, 0.5)
right.material.color = Color(0.5, 1, 0.1)
right.material.diffuse = 0.7
right.material.specular = 0.3

left = Sphere()
left.translation(-1.5, 0.33, -0.75).scaling(0.33, 0.33, 0.33)
left.material.color = Color(1, 0.8, 1)
left.material.diffuse = 0.7
left.material.specular = 0.3

light = PointLight(Color(1, 1, 1), Point(-10, 10, -10))
world = World()
world.objects = [floor, left_wall, right_wall, middle, left, right]
world.light = light

transform = ViewTransformer.view_transform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))
camera = Camera(1000, 500, pi / 3, transform)
canvas = Renderer.render(camera, world)

ppm = PPMWriter.write_ppm_from_canvas(canvas)
with open('out/world_basic.ppm', 'w') as f:
    f.write('\n'.join(ppm))