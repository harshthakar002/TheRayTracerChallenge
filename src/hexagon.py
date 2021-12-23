from math import pi
from physical.point_light import PointLight
from features.color import Color
from features.point import Point
from physical.world import World
from transformations.view_transformer import ViewTransformer
from features.vector import Vector
from physical.camera import Camera
from physical.renderer import Renderer
from canvas.ppm_writer import PPMWriter
from figures.shape import Shape
from figures.sphere import Sphere
from figures.cylinder import Cylinder
from figures.group import Group
from datetime import date, datetime

begin_time = datetime.now()

def hexagon_corner() -> Shape:
    corner = Sphere()
    corner.translation(0, 0, -1).scaling(0.25, 0.25, 0.25)
    return corner

def hexagon_edge() -> Shape:
    edge = Cylinder()
    edge.minimum = 0
    edge.maximum = 1
    edge.translation(0, 0, -1).rotation_y(-pi / 6).rotation_z(-pi / 2).scaling(0.25, 1, 0.25)
    return edge

def hexagon_side() ->  Group:
    side = Group()
    side.add_child(hexagon_corner())
    side.add_child(hexagon_edge())
    return side

hex = Group()
for n in range(6):
    side = hexagon_side()
    side.rotation_y(n * pi / 3)
    hex.add_child(side)

hex.translation(0, 1, 0).rotation_x(-pi / 4)

light = PointLight(Color(1, 1, 1), Point(-10, 10, -10))
world = World()
world.objects = [hex]
world.light = light

transform = ViewTransformer.view_transform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))
camera = Camera(500, 250, pi / 3, transform)
canvas = Renderer.render(camera, world)

ppm = PPMWriter.write_ppm_from_canvas(canvas)
with open('out/hexagon.ppm', 'w') as f:
    f.write('\n'.join(ppm))

end_time = datetime.now()
print("Rendering started at:")
print(begin_time)
print("Rendering finished at:")
print(end_time)
print("Time taken for rendering:")
print(end_time - begin_time)
