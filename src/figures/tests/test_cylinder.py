from features.bounds import Bounds
from features.point import Point
from features.vector import Vector
from figures.cylinder import Cylinder
from figures.ray import Ray
from figures.intersection import Intersection
from features.equality import is_approximately_equal
from math import inf

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

def test_normal_on_cylinder():
    cyl = Cylinder()
    n = cyl.local_normal_at(Point(1, 0, 0), None, None)
    assert n == Vector(1, 0, 0)
    n = cyl.local_normal_at(Point(0, 5, -1), None, None)
    assert n == Vector(0, 0, -1)
    n = cyl.local_normal_at(Point(0, -2, 1), None, None)
    assert n == Vector(0, 0, 1)
    n = cyl.local_normal_at(Point(-1, 1, 0), None, None)
    assert n == Vector(-1, 0, 0)

def test_default_minimum_and_maximun_for_a_cylinder():
    cyl = Cylinder()
    assert cyl.minimum == -inf
    assert cyl.maximum == inf

def test_intersecting_a_constrained_cylinder():
    cyl = Cylinder(1, 2)
    r = Ray(Point(0, 1.5, 0), Vector(0.1, 1, 0).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 0
    r = Ray(Point(0, 3, -5), Vector(0, 0, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 0
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 0
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 0
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 0
    r = Ray(Point(0, 1.5, -2), Vector(0, 0, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 2

def test_default_closed_value_for_cylinder():
    cyl = Cylinder()
    assert not cyl.closed

def test_intersecting_caps_of_a_closed_cylinder():
    cyl = Cylinder(1, 2, True)
    r = Ray(Point(0, 3, 0), Vector(0, -1, 0).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 2
    r = Ray(Point(0, 3, -2), Vector(0, -1, 2).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 2
    r = Ray(Point(0, 4, -2), Vector(0, -1, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 2
    r = Ray(Point(0, 0, -2), Vector(0, 1, 2).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 2
    r = Ray(Point(0, -1, -2), Vector(0, 1, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, cyl)
    assert len(xs) == 2

def test_normal_vector_on_cylinder_end_caps():
    cyl = Cylinder(1, 2, True)
    n = cyl.local_normal_at(Point(0, 1, 0), None, None)
    assert n == Vector(0, -1, 0)
    n = cyl.local_normal_at(Point(0.5, 1, 0), None, None)
    assert n == Vector(0, -1, 0)
    n = cyl.local_normal_at(Point(0, 1, 0.5), None, None)
    assert n == Vector(0, -1, 0)
    n = cyl.local_normal_at(Point(0, 2, 0), None, None)
    assert n == Vector(0, 1, 0)
    n = cyl.local_normal_at(Point(0.5, 2, 0), None, None)
    assert n == Vector(0, 1, 0)
    n = cyl.local_normal_at(Point(0, 2, 0.5), None, None)
    assert n == Vector(0, 1, 0)

def test_bounds_on_infinte_cylinder():
    cyl = Cylinder()
    assert cyl.bounds() == Bounds(-1, -inf, -1, 1, inf, 1)

def test_bounds_on_closed_cylinder():
    cyl = Cylinder(1, 2, True)
    assert cyl.bounds() == Bounds(-1, 1, -1, 1, 2, 1)