from math import pi
from features.bounds import Bounds
from figures.group import Group
from physical.point_light import PointLight
from features.color import Color
from features.point import Point
from physical.world import World
from transformations.view_transformer import ViewTransformer
from features.vector import Vector
from physical.camera import Camera
from physical.renderer import Renderer
from canvas.ppm_writer import PPMWriter
from wavefront.obj_parser import ObjParser
from datetime import datetime

begin_time = datetime.now()
print("Parsing started.")
teapot_obj_parser = ObjParser('obj_files//teapot.obj')
teapot_parsed_obj = teapot_obj_parser.parse()
parsing_time = datetime.now()
print("Parsing complete. Parsing time taken:")
print(parsing_time - begin_time)

teapot_group = teapot_parsed_obj.asGroup()
teapot_group = teapot_parsed_obj.asGroup()

n = 7

bounds = teapot_group.bounds()
delta = bounds.max_point - bounds.min_point
mat: list[list[list[Group]]] = []
for i in range(n):
    mat.append([])
    for j in range(n):
        mat[i].append([])
        for k in range(n):
            mat[i][j].append(Group('Group' + str(i) + str(j) + str(k)))

dx, dy, dz = delta.x / n, delta.y / n, delta.z / n

for shape in teapot_group.shapes[0].shapes:
    s_bounds: Bounds = shape.bounds()
    s_mid = (s_bounds.max_point + s_bounds.min_point) / 2
    mat[int(s_mid.x / dx)][int(s_mid.y / dy)][int(s_mid.z / dz)].add_child(shape)

split_group = Group('teapot_split')

for i in range(n):
    for j in range(n):
        for k in range(n):
            split_group.add_child(mat[i][j][k])

split_group = split_group.scaling(0.8, 0.8, 0.8)

light = PointLight(Color(1, 1, 1), Point(-10, 10, -10))
world = World()
world.objects = [split_group]
world.light = light
print("Rendering started.")
transform = ViewTransformer.view_transform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))
camera = Camera(250, 250, pi / 3, transform)
canvas = Renderer.render(camera, world)

print("Rendering complete. Rendering time taken:")
print(datetime.now() - parsing_time)

ppm = PPMWriter.write_ppm_from_canvas(canvas)
with open('out/teapot.ppm', 'w') as f:
    f.write('\n'.join(ppm))

end_time = datetime.now()
print("Rendering started at:")
print(begin_time)   
print("Rendering finished at:")
print(end_time)
print("Time taken for rendering:")
print(end_time - begin_time)
