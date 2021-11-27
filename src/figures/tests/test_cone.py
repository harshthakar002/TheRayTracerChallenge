from figures.cone import Cone
from figures.ray import Ray
from features.point import Point
from features.vector import Vector
from features.equality import is_approximately_equal
from figures.intersection import Intersection

def test_intersecting_cone_with_ray():
    shape = Cone()
    ray = Ray(Point(0, 0, -5), Vector(0, 0, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(ray, shape)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 5)
    assert is_approximately_equal(xs[1].t, 5)
    ray = Ray(Point(0, 0, -5), Vector(1, 1, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(ray, shape)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 8.66025)
    assert is_approximately_equal(xs[1].t, 8.66025)
    ray = Ray(Point(1, 1, -5), Vector(-0.5, -1, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(ray, shape)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 4.55006)
    assert is_approximately_equal(xs[1].t, 49.44994)

def test_intersecting_cone_with_ray_parallel_to_one_of_the_halves():
    shape = Cone()
    r = Ray(Point(0, 0, -1), Vector(0, 1, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, shape)
    assert len(xs) == 1
    assert is_approximately_equal(xs[0].t, 0.35355)

def test_intersecting_cone_end_caps():
    shape = Cone(-0.5, 0.5, True)
    r = Ray(Point(0, 0, -5), Vector(0, 1, 0).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, shape)
    assert len(xs) == 0
    r = Ray(Point(0, 0, -0.25), Vector(0, 1, 1).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, shape)
    assert len(xs) == 2
    r = Ray(Point(0, 0, -0.25), Vector(0, 1, 0).normalize())
    xs = Intersection.find_intersections_of_ray_and_figure(r, shape)
    assert len(xs) == 4
