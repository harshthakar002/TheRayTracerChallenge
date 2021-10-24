from features.vector import Vector
from figures.ray import Ray
from figures.sphere import Sphere
from features.point import Point
from features.vector import Vector
from features.equality import is_approximately_equal

def test_ray_intersects_sphere_at_two_points():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.ray_intersection_distance(r)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0], 4.0)
    assert is_approximately_equal(xs[1], 6.0)

def test_ray_intersects_sphere_at_tangent():
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.ray_intersection_distance(r)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0], 5.0)
    assert is_approximately_equal(xs[1], 5.0)

def test_ray_misses_sphere():
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.ray_intersection_distance(r)
    assert len(xs) == 0

def test_ray_originates_in_sphere():
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    s = Sphere()
    xs = s.ray_intersection_distance(r)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0], -1)
    assert is_approximately_equal(xs[1], 1)

def test_sphere_is_behind_ray():
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.ray_intersection_distance(r)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0], -6)
    assert is_approximately_equal(xs[1], -4)