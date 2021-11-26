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
from patterns.stripe_pattern import StripePattern
from transformations.transformer import Transformer
from patterns.gradient_pattern import GradientPattern
from patterns.ring_pattern import RingPattern
from patterns.checker_pattern import CheckerPattern
from patterns.solid_pattern import SolidPattern
from patterns.blended_pattern import BlendedPattern

floor = Plane()
floor.material.color = Color(1, 0.9, 0.9)
pattern1 = CheckerPattern(SolidPattern(Color(1, 0.9, 0.9)), SolidPattern(Color(0, 0.1, 0.1)))
pattern1.scaling(0.1, 0.1, 0.1)
pattern2 = CheckerPattern(SolidPattern(Color(1, 0.9, 0.9)), SolidPattern(Color(1, 0.1, 0.1)))
pattern2.scaling(0.1, 0.1, 0.1)
floor.material.pattern = CheckerPattern(pattern1, pattern2)
floor.material.specular = 1

left_wall = Plane()
left_wall.translation(0, 0, 5).rotation_y(-pi / 4).rotation_x(pi / 2)
left_wall.material.color = Color(1, 0.9, 0.9)
left_wall.material.pattern = CheckerPattern(RingPattern(SolidPattern(Color(1, 0.9, 0.9)), SolidPattern(Color(0, 0.1, 0.1))), CheckerPattern(SolidPattern(Color(1, 0.9, 0.9)), SolidPattern(Color(0, 0.1, 0.1))))
left_wall.material.specular = 1

right_wall = Plane()
right_wall.translation(0, 0, 5).rotation_y(pi / 4).rotation_x(pi / 2)
right_wall.material.color = Color(1, 0.9, 0.9)
right_wall.material.pattern = RingPattern(SolidPattern(Color(1, 0.9, 0.9)), SolidPattern(Color(0, 0.1, 0.1)))
right_wall.material.specular = 1

middle = Sphere()
middle.translation(-0.5, 1, 0.5)
middle.material.color = Color(0, 0, 1)
pattern1 = CheckerPattern(SolidPattern(Color(0, 0, 1)), SolidPattern(Color(1, 1, 1)))
pattern2 = CheckerPattern(SolidPattern(Color(1, 0, 0)), SolidPattern(Color(0, 0, 0)))
pattern2.scaling(0.3, 0.3, 0.3)
middle.material.pattern = BlendedPattern(pattern1, pattern2)
middle.material.pattern.scaling(0.5, 0.5, 0.5)
middle.material.diffuse = 1
middle.material.specular = 1

right = Sphere()
right.translation(1.5, 0.5, -0.5).scaling(0.5, 0.5, 0.5)
right.material.color = Color(0.0, 1, 0.0)
right.material.pattern = GradientPattern(SolidPattern(Color(0, 1, 0)), SolidPattern(Color(0, 0, 1)))
right.material.pattern.scaling(0.4, 0.4, 0.4)
right.material.diffuse = 1
right.material.specular = 1

left = Sphere()
left.translation(-1.5, 0.33, -0.75).scaling(0.33, 0.33, 0.33)
left.material.color = Color(1, 0, 0)
left.material.pattern = StripePattern(SolidPattern(Color(1, 0, 0)), SolidPattern(Color(1, 1, 1)))
left.material.pattern.scaling(0.1, 0.1, 0.1).rotation_z(pi / 2)
left.material.diffuse = 1
left.material.specular = 1

light = PointLight(Color(1, 1, 1), Point(-10, 10, -10))
world = World()
world.objects = [floor, left_wall, right_wall, middle, left, right]
world.light = light

transform = ViewTransformer.view_transform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))
camera = Camera(500, 250, pi / 3, transform)
canvas = Renderer.render(camera, world)

ppm = PPMWriter.write_ppm_from_canvas(canvas)
with open('out/pattern_basic.ppm', 'w') as f:
    f.write('\n'.join(ppm))