from features.point import Point
from features.vector import Vector
from figures.cylinder import Cylinder
from figures.ray import Ray
from figures.intersection import Intersection
from features.equality import is_approximately_equal

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

def test_ray_strikes_cylinder():
    cyl = Cylinder()
    ray = Ray(Point(1, 0, -5), Vector(0, 0, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(ray, cyl)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 5)
    assert is_approximately_equal(xs[1].t, 5)
    ray = Ray(Point(0, 0, -5), Vector(0, 0, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(ray, cyl)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 4)
    assert is_approximately_equal(xs[1].t, 6)
    ray = Ray(Point(0.5, 0, -5), Vector(0.1, 1, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(ray, cyl)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 6.80798)
    assert is_approximately_equal(xs[1].t, 7.08872)