from features.point import Point
from features.vector import Vector
from figures.intersection import Intersection
from figures.ray import Ray
from figures.triangle import Triangle

def test_constructing_a_triange():
    p1 = Point(0, 1, 0)
    p2 = Point(-1, 0, 0)
    p3 = Point(1, 0, 0)
    t = Triangle(p1, p2, p3)
    assert t.p1 == p1
    assert t.p2 == p2
    assert t.p3 == p3
    assert t.e1 == Vector(-1, -1, 0)
    assert t.e2 == Vector(1, -1, 0)
    assert t.normal == Vector(0, 0, -1)

def test_normal_on_a_triange():
    t = Triangle(Point(0, 1, 0), Point(-1, 0, 0), Point(1, 0, 0))
    n1 = t.local_normal_at(Point(0, 0.5, 0))
    n2 = t.local_normal_at(Point(-0.5, 0.75, 0))
    n3 = t.local_normal_at(Point(0.5, 0.25, 0))
    assert n1 == t.normal
    assert n2 == t.normal
    assert n3 == t.normal

def test_intersection_ray_parallel_to_triangle():
    t = Triangle(Point(0, 1, 0), Point(-1, 0, 0), Point(1, 0, 0))
    r = Ray(Point(0, -1, -2), Vector(0, 1, 0))
    xs = Intersection.find_intersections_of_ray_and_figure(r, t)
    assert len(xs) == 0

def test_intersection_ray_misses_p1_p3_edge():
    t = Triangle(Point(0, 1, 0), Point(-1, 0, 0), Point(1, 0, 0))
    r = Ray(Point(1, 1, -2), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, t)
    assert len(xs) == 0

def test_intersection_ray_misses_p1_p2_edge():
    t = Triangle(Point(0, 1, 0), Point(-1, 0, 0), Point(1, 0, 0))
    r = Ray(Point(-1, 1, -2), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, t)
    assert len(xs) == 0

def test_intersection_ray_misses_p2_p3_edge():
    t = Triangle(Point(0, 1, 0), Point(-1, 0, 0), Point(1, 0, 0))
    r = Ray(Point(0, -1, -2), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, t)
    assert len(xs) == 0