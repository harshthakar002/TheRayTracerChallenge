from figures.cube import Cube
from figures.ray import Ray
from features.point import Point
from features.vector import Vector
from features.equality import is_approximately_equal
from figures.intersection import Intersection

def test_ray_intersects_a_cube():
    c = Cube()
    r = Ray(Point(5, 0.5, 0), Vector(-1, 0, 0))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 4.0)
    assert is_approximately_equal(xs[1].t, 6.0)
    r = Ray(Point(-5, 0.5, 0), Vector(1, 0, 0))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 4.0)
    assert is_approximately_equal(xs[1].t, 6.0)
    r = Ray(Point(0.5, 5, 0), Vector(0, -1, 0))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 4.0)
    assert is_approximately_equal(xs[1].t, 6.0)
    r = Ray(Point(0.5, -5, 0), Vector(0, 1, 0))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 4.0)
    assert is_approximately_equal(xs[1].t, 6.0)
    r = Ray(Point(0.5, 0, 5), Vector(0, 0, -1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 4.0)
    assert is_approximately_equal(xs[1].t, 6.0)
    r = Ray(Point(0.5, 0, -5), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 4.0)
    assert is_approximately_equal(xs[1].t, 6.0)
    r = Ray(Point(0, 0.5, 0), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, -1)
    assert is_approximately_equal(xs[1].t, 1)