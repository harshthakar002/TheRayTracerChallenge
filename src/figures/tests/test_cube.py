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

def test_a_ray_misses_a_cube():
    c = Cube()
    r = Ray(Point(-2, 0, 0), Vector(0.2673, 0.5345, 0.8018))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 0
    r = Ray(Point(0, -2, 0), Vector(0.8018, 0.2673, 0.5345))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 0
    r = Ray(Point(0, 0, -2), Vector(0.5345, 0.8018, 0.2673))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 0
    r = Ray(Point(2, 0, 2), Vector(0, 0, -1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 0
    r = Ray(Point(0, 2, 2), Vector(0, -1, 0))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 0
    r = Ray(Point(2, 2, 0), Vector(-1, 0, 0))
    xs = Intersection.find_intersections_of_ray_and_figure(r, c)
    assert len(xs) == 0

def test_normal_on_surface_of_the_cube():
    c = Cube()
    p = Point(1, 0.5, -0.8)
    normal = c.local_normal_at(p)
    assert normal == Vector(1, 0, 0)
    p = Point(-1, -0.2, 0.9)
    normal = c.local_normal_at(p)
    assert normal == Vector(-1, 0, 0)
    p = Point(-0.4, 1, -0.1)
    normal = c.local_normal_at(p)
    assert normal == Vector(0, 1, 0)
    p = Point(0.3, -1, -0.7)
    normal = c.local_normal_at(p)
    assert normal == Vector(0, -1, 0)
    p = Point(-0.6, 0.3, 1)
    normal = c.local_normal_at(p)
    assert normal == Vector(0, 0, 1)
    p = Point(0.4, 0.4, -1)
    normal = c.local_normal_at(p)
    assert normal == Vector(0, 0, -1)
    p = Point(1, 1, 1)
    normal = c.local_normal_at(p)
    assert normal == Vector(1, 0, 0)
    p = Point(-1, -1, -1)
    normal = c.local_normal_at(p)
    assert normal == Vector(-1, 0, 0)