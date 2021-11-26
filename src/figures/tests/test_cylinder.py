from features.point import Point
from features.vector import Vector
from figures.cylinder import Cylinder
from figures.ray import Ray
from figures.intersection import Intersection

def test_ray_misses_cylinder():
    cyl = Cylinder()
    ray = Ray(Point(1, 0, 0), Vector(0, 1, 0).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(ray, cyl)
    assert len(xs) == 0
    ray = Ray(Point(0, 0, 0), Vector(0, 1, 0).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(ray, cyl)
    assert len(xs) == 0
    ray = Ray(Point(0, 0, -5), Vector(1, 1, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(ray, cyl)
    assert len(xs) == 0