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
from wavefront.obj_parser import ObjParser
from datetime import datetime

begin_time = datetime.now()
print("Parsing started.")
cow_obj_parser = ObjParser('obj_files//cow_grouped.obj')
cow_parsed_obj = cow_obj_parser.parse()
parsing_time = datetime.now()
print("Parsing complete. Parsing time taken:")
print(parsing_time - begin_time)

cow_group = cow_parsed_obj.asGroup()
cow_group = cow_group.scaling(0.3, 0.3, 0.3).translation(1, 1, 1)

light = PointLight(Color(1, 1, 1), Point(-10, 10, -10))
world = World()
world.objects = [cow_group]
world.light = light
print("Rendering started.")
transform = ViewTransformer.view_transform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))
camera = Camera(500, 250, pi / 3, transform)
canvas = Renderer.render(camera, world)

print("Rendering complete. Rendering time taken:")
print(datetime.now() - parsing_time)

ppm = PPMWriter.write_ppm_from_canvas(canvas)
with open('out/cow.ppm', 'w') as f:
    f.write('\n'.join(ppm))

end_time = datetime.now()
print("Rendering started at:")
print(begin_time)   
print("Rendering finished at:")
print(end_time)
print("Time taken for rendering:")
print(end_time - begin_time)
