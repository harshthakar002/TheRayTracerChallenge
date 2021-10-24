from figures.ray import Ray
from figures.sphere import Sphere
from canvas.canvas import Canvas
from features.point import Point
from features.vector import Vector
from features.color import Color
from physical.lighter import Lighter
from transformations.figure_transformer import FigureTransformer
from figures.intersection import Intersection
from canvas.ppm_writer import PPMWriter
from physical.point_light import PointLight

s = Sphere()
origin_t, direction_t = FigureTransformer.scaling(100, 100, 100)
s.set_transform(origin_t, direction_t)
origin_t, direction_t = FigureTransformer.translation(0, 0, 40)
s.set_transform(origin_t, direction_t)
s.material.color = Color(1, 0.2, 1)

light = PointLight(Color(1, 1, 1), Point(-10, 10, -10))

c = Canvas(500, 500)
for i in range(-250, 250):
    for j in range(-250, 250):
        ray = Ray(Point(0, 0, -5), Vector(i, j, 10).normalize())
        intersections = Intersection.find_intersections_of_ray_and_figure(ray, s)
        hit = Intersection.calculate_hit(intersections)
        if hit != None:
            point = ray.position (hit.t)
            normal = hit.object.normal_at(point)
            eye = ray.direction.negate()
            color = Lighter.lighting(hit.object.material, light, point, eye, normal)
            c.write_pixel(i + 250, j + 250, Color(1, 1, 1))

ppm = PPMWriter.write_ppm_from_canvas(c)
with open('out/sphere_shadow.ppm', 'w') as f:
    f.write('\n'.join(ppm))
