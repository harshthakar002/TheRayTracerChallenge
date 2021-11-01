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
origin_transform, direction_transform = FigureTransformer.scaling(10, 0.01, 10)
floor.set_transform(origin_transform, direction_transform)
floor.material.color = Color(1, 0.9, 0.9)
floor.material.specular = 0

left_wall = Sphere()
origin_transform, direction_transform = FigureTransformer.translation(0, 0, 5)
left_wall.set_transform(origin_transform, direction_transform)
origin_transform, direction_transform = FigureTransformer.rotation_y(-pi / 4)
left_wall.set_transform(origin_transform, direction_transform)
origin_transform, direction_transform = FigureTransformer.rotation_x(pi / 2)
left_wall.set_transform(origin_transform, direction_transform)
origin_transform, direction_transform = FigureTransformer.scaling(10, 0.01, 10)
left_wall.set_transform(origin_transform, direction_transform)
left_wall.material = floor.material

right_wall = Sphere()
origin_transform, direction_transform = FigureTransformer.translation(0, 0, 5)
right_wall.set_transform(origin_transform, direction_transform)
origin_transform, direction_transform = FigureTransformer.rotation_y(pi / 4)
right_wall.set_transform(origin_transform, direction_transform)
origin_transform, direction_transform = FigureTransformer.rotation_x(pi / 2)
right_wall.set_transform(origin_transform, direction_transform)
origin_transform, direction_transform = FigureTransformer.scaling(10, 0.01, 10)
right_wall.set_transform(origin_transform, direction_transform)
right_wall.material = floor.material

middle = Sphere()
origin_transform, direction_transform = FigureTransformer.translation(-0.5, 1, 0.5)
middle.set_transform(origin_transform, direction_transform)
middle.material.color = Color(0.1, 1, 0.5)
middle.material.diffuse = 0.7
middle.material.specular = 0.3

right = Sphere()
origin_transform, direction_transform = FigureTransformer.translation(1.5, 0.5, -0.5)
right.set_transform(origin_transform, direction_transform)
origin_transform, direction_transform = FigureTransformer.scaling(0.5, 0.5, 0.5)
right.set_transform(origin_transform, direction_transform)
right.material.color = Color(0.5, 1, 0.1)
right.material.diffuse = 0.7
right.material.specular = 0.3

left = Sphere()
origin_transform, direction_transform = FigureTransformer.translation(-1.5, 0.33, -0.75)
left.set_transform(origin_transform, direction_transform)
origin_transform, direction_transform = FigureTransformer.scaling(0.33, 0.33, 0.33)
left.set_transform(origin_transform, direction_transform)
left.material.color = Color(1, 0.8, 1)
left.material.diffuse = 0.7
left.material.specular = 0.3

light = PointLight(Color(1, 1, 1), Point(-10, 10, -10))
world = World()
world.objects = [floor, left_wall, right_wall, middle, left, right]
world.light = light

transform = ViewTransformer.view_transform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))
camera = Camera(100, 50, pi / 3, transform)
canvas = Renderer.render(camera, world)

ppm = PPMWriter.write_ppm_from_canvas(canvas)
with open('out/world_basic.ppm', 'w') as f:
    f.write('\n'.join(ppm))