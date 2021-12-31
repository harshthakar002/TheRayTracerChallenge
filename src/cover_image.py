from canvas.ppm_writer import PPMWriter
from features.color import WHITE_COLOR, Color
from features.point import Point
from features.vector import Vector
from figures.cube import Cube
from figures.group import Group
from figures.plane import Plane
from figures.sphere import Sphere
from math import pi
from physical.camera import Camera
from physical.material import Material
from physical.point_light import PointLight
from physical.renderer import Renderer
from physical.world import World
from transformations.view_transformer import ViewTransformer

# Camera
view_transform = ViewTransformer.view_transform(Point(-6, 6, -10), Point(6, 0, 6), Vector(-0.45, 1, 0))
camera = Camera(250, 250, pi / 3, view_transform)

# Light Source
light = PointLight(WHITE_COLOR, Point(50, 100, -50))

# Some constants
white_material = Material(color=WHITE_COLOR, ambient=0.1, diffuse=0.7, specular=0.0, reflective=0.1)
blue_material = Material(color=Color(0.537, 0.831, 0.914), ambient=0.1, diffuse=0.7, specular=0.0, reflective=0.1)
red_material = Material(color=Color(0.941, 0.322, 0.388), ambient=0.1, diffuse=0.7, specular=0.0, reflective=0.1)
purple_material = Material(color=Color(0.373, 0.404, 0.550), ambient=0.1, diffuse=0.7, specular=0.0, reflective=0.1)

objects = []

# Backdrop
backdrop_material = Material(color=WHITE_COLOR, ambient=1, diffuse=0, specular=0)
backdrop = Plane()
backdrop.material = backdrop_material
backdrop.rotation_x(pi / 2).translation(0, 0, 500)

# Elements of scene
sphere_material = Material(color=Color(0.373, 0.404, 0.550), ambient=0, diffuse=0.2, specular=1, shininess=200, reflective=0.7, transparency=0.7, refractive_index=1.5)
sphere = Sphere()
sphere.material = sphere_material
sphere.scaling(3.5, 3.5, 3.5) # large-object
objects.append(sphere)

cube1 = Cube()
cube1.material = white_material
cube1.scaling(3, 3, 3).translation(4, 0, 0) # medium-object
objects.append(cube1)

cube2 = Cube()
cube2.material = blue_material
cube2.scaling(3.5, 3.5, 3.5).translation(8.5, 1.5, -0.5)
objects.append(cube2)

cube3 = Cube()
cube3.material = red_material
cube3.scaling(3.5, 3.5, 3.5).translation(0, 0, 4)
objects.append(cube3)

cube4 = Cube()
cube4.material = white_material
cube4.scaling(2, 2, 2).translation(4, 0, 4) # small-object
objects.append(cube4)

cube5 = Cube()
cube5.material = purple_material
cube5.scaling(3, 3, 3).translation(7.5, 0.5, 4)
objects.append(cube5)

cube6 = Cube()
cube6.material = white_material
cube6.scaling(3, 3, 3).translation(-0.25, 0.25, 8)
objects.append(cube6)

cube7 = Cube()
cube7.material = purple_material
cube7.scaling(3.5, 3.5, 3.5).translation(4, 1, 7.5) 
objects.append(cube7)

cube8 = Cube()
cube8.material = red_material
cube8.scaling(3, 3, 3).translation(10, 2, 7.5)
objects.append(cube8)

cube9 = Cube()
cube9.material = white_material
cube9.scaling(2, 2, 2).translation(8, 2, 12)
objects.append(cube9)

cube10 = Cube()
cube10.material = white_material
cube10.scaling(2, 2, 2).translation(20, 1, 9)
objects.append(cube10)

cube11 = Cube()
cube11.material = blue_material
cube11.scaling(3.5, 3.5, 3.5).translation(-0.5, -5, 0.25)
objects.append(cube11)

cube12 = Cube()
cube12.material = red_material
cube12.scaling(3.5, 3.5, 3.5).translation(4, -4, 0)
objects.append(cube12)

cube13 = Cube()
cube13.material = white_material
cube13.scaling(3.5, 3.5, 3.5).translation(8.5, -4, 0)
objects.append(cube13)

cube14 = Cube()
cube14.material = white_material
cube14.scaling(3.5, 3.5, 3.5).translation(0, -4, 4)
objects.append(cube14)

cube15 = Cube()
cube15.material = purple_material
cube15.scaling(3.5, 3.5, 3.5).translation(-0.5, -4.5, 8)
objects.append(cube15)

cube16 = Cube()
cube16.material = white_material
cube16.scaling(3.5, 3.5, 3.5).translation(0, -8, 4)
objects.append(cube16)

cube17 = Cube()
cube17.material = white_material
cube17.scaling(3.5, 3.5, 3.5).translation(-0.5, -8.5, 8)
objects.append(cube17)

group = Group()
group.translation(1, -1, 1).scaling(0.5, 0.5, 0.5)
for object in objects:
    group.add_child(object)

world = World()
world.objects = [backdrop, group]
world.light = light 
canvas = Renderer.render(camera, world)

ppm = PPMWriter.write_ppm_from_canvas(canvas)
with open('out/cover_image.ppm', 'w') as f:
    f.write('\n'.join(ppm))