from figures.ray import Ray
from figures.sphere import Sphere
from canvas.canvas import Canvas
from features.point import Point
from features.vector import Vector
from features.color import Color
from physical.shader import Shader
from transformations.figure_transformer import FigureTransformer
from figures.intersection import Intersection
from canvas.ppm_writer import PPMWriter
from physical.point_light import PointLight

s = Sphere()
s.material.color = Color(1, 0.2, 1)

light = PointLight(Color(1, 1, 1), Point(-10, 10, -10))

c = Canvas(100, 100)
wall_size = 7.0 
pixel_size = 7.0 / 100
half = wall_size / 2 
color = Color(1, 0, 0)
ray_origin = Point(0, 0, -5)
wall_z = 10

for y in range(100):
    world_y = half - (pixel_size * y)
    for x in range (100):
        world_x = -half + (pixel_size * x)
        position = Point(world_x, world_y, wall_z)
        direction = position - ray_origin
        r = Ray(ray_origin, Vector(direction.x, direction.y, direction.z).normalize())
        xs = Intersection.find_intersections_of_ray_and_figure(r, s)
        hit = Intersection.calculate_hit(xs)
        if hit == None:
            continue
        point = r.position(hit.t)
        normal = s.normal_at(point)
        eye = r.direction.negate()
        color = Shader.lighting(hit.object.material, light, point, eye, normal, False)
        c.write_pixel(x, y, color)
        
ppm = PPMWriter.write_ppm_from_canvas(c)
with open('out/sphere_shadow.ppm', 'w') as f:
    f.write('\n'.join(ppm))
