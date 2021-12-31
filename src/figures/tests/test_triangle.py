from features.equality import is_approximately_equal
from features.point import Point
from features.vector import Vector
from figures.intersection import Intersection
from figures.ray import Ray
from figures.triangle import SmoothTriangle, Triangle

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
    n1 = t.local_normal_at(Point(0, 0.5, 0), None, None)
    n2 = t.local_normal_at(Point(-0.5, 0.75, 0), None, None)
    n3 = t.local_normal_at(Point(0.5, 0.25, 0), None, None)
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

def test_ray_strikes_a_triange():
    t = Triangle(Point(0, 1, 0), Point(-1, 0, 0), Point(1, 0, 0))
    r = Ray(Point(0, 0.5, -2), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, t)
    assert len(xs) == 1
    assert is_approximately_equal(xs[0].t, 2)

def test_constuct_smooth_triangle():
    p1 = Point(0, 1, 0)
    p2 = Point(-1, 0, 0)
    p3 = Point(1, 0, 0)
    n1 = Vector(0, 1, 0)
    n2 = Vector(-1, 0, 0)
    n3 = Vector(1, 0, 0)
    t = SmoothTriangle(p1, p2, p3, n1, n2, n3)
    assert t.p1 == p1
    assert t.p2 == p2
    assert t.p3 == p3
    assert t.n1 == n1
    assert t.n2 == n2
    assert t.n3 == n3

def test_intersect_smooth_triangle_stores_u_and_v():
    p1 = Point(0, 1, 0)
    p2 = Point(-1, 0, 0)
    p3 = Point(1, 0, 0)
    n1 = Vector(0, 1, 0)
    n2 = Vector(-1, 0, 0)
    n3 = Vector(1, 0, 0)
    t = SmoothTriangle(p1, p2, p3, n1, n2, n3)
    r = Ray(Point(-0.2, 0.3,-2), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, t)
    assert is_approximately_equal(xs[0].u, 0.45)
    assert is_approximately_equal(xs[0].v, 0.25)

def test_smooth_triangle_uses_u_and_v_to_interpolate_the_normal():
    p1 = Point(0, 1, 0)
    p2 = Point(-1, 0, 0)
    p3 = Point(1, 0, 0)
    n1 = Vector(0, 1, 0)
    n2 = Vector(-1, 0, 0)
    n3 = Vector(1, 0, 0)
    t = SmoothTriangle(p1, p2, p3, n1, n2, n3)
    i = Intersection(1, t, 0.45, 0.25)
    n = t.normal_at(Point(0, 0, 0), i.u, i.v)
    assert n == Vector(-0.5547, 0.83205, 0)