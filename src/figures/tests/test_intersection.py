from figures.intersection import Intersection
from figures.sphere import Sphere
from features.equality import is_approximately_equal
from figures.ray import Ray
from features.point import Point
from features.vector import Vector

def test_intersection_creation():
    s = Sphere()
    i = Intersection(3.5, s)
    assert is_approximately_equal(i.t, 3.5)
    assert i.object == s

def test_intersect_sets_object_on_intersection():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = Intersection.find_intersections_of_ray_and_figure(r, s)
    assert len(xs) == 2
    assert xs[0].object == s
    assert is_approximately_equal(xs[0].t, 4.0)
    assert is_approximately_equal(xs[1].t, 6.0)
    assert xs[1].object == s