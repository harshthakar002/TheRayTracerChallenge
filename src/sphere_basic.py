from figures.ray import Ray
from figures.sphere import Sphere
from canvas.canvas import Canvas
from features.point import Point
from features.vector import Vector
from features.color import Color
from transformations.figure_transformer import FigureTransformer
from figures.intersection import Intersection
from canvas.ppm_writer import PPMWriter

s = Sphere()
origin_t, direction_t = FigureTransformer.scaling(20, 20, 20)
s.set_transform(origin_t, direction_t)
origin_t, direction_t = FigureTransformer.translation(0, 0, 40)
s.set_transform(origin_t, direction_t)

c = Canvas(500, 500)
for i in range(-250, 250):
    for j in range(-250, 250):
        ray = Ray(Point(0, 0, 0), Vector(i, j, 100).normalize())
        intersections = Intersection.find_intersections_of_ray_and_figure(ray, s)
        hits = Intersection.calculate_hit(intersections)
        if len(hits) != 0:
            c.write_pixel(i + 250, j + 250, Color(0.8, 0.2, 0.4))
        else:
            c.write_pixel(i + 250, j + 250, Color(1, 1, 1))

ppm = PPMWriter.write_ppm_from_canvas(c)
with open('out/sphere_shadow.ppm', 'w') as f:
    f.write('\n'.join(ppm))
