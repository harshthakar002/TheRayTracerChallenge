from features.point import Point
from features.vector import Vector
from figures.intersection import Intersection
from figures.plane import Plane
from figures.ray import Ray

def test_normal_of_plane_is_constant_everywhere():
    p = Plane()
    n1 = p.local_normal_at(Point(0, 0, 0))
    n2 = p.local_normal_at(Point(10, 0, -10))
    n3 = p.local_normal_at(Point(-5, 0, 150))
    assert n1 == Vector(0, 1, 0)
    assert n2 == Vector(0, 1, 0)
    assert n3 == Vector(0, 1, 0)

def test_intersect_with_ray_parallel_to_plane():
    p = Plane()
    r = Ray(Point(0, 10, 0), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, p)
    assert len(xs) == 0

def test_intersect_with_coplanar_ray():
    p = Plane()
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, p)
    assert len(xs) == 0

def test_intersect_plane_from_above():
    p = Plane()
    r = Ray(Point(0, 1, 0), Vector(0, -1, 0))
    xs = Intersection.find_intersections_of_ray_and_figure(r, p)
    assert len(xs) == 1
    assert xs[0].t == 1
    assert xs[0].object == p

def test_intersect_plane_from_below():
    p = Plane()
    r = Ray(Point(0, -1, 0), Vector(0, 1, 0))
    xs = Intersection.find_intersections_of_ray_and_figure(r, p)
    assert len(xs) == 1
    assert xs[0].t == 1
    assert xs[0].object == p