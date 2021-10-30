from figures.intersection import Intersection
from figures.sphere import Sphere
from features.equality import is_approximately_equal
from figures.ray import Ray
from features.point import Point
from features.vector import Vector
from physical.default_world import DefaultWorld

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

def test_hit_all_positive_t():
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = [i2, i1]
    i = Intersection.calculate_hit(xs)
    assert i == i1

def test_hit_positive_negative_t():
    s = Sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(1, s)
    xs = [i2, i1]
    i = Intersection.calculate_hit(xs)
    assert i == i2

def test_hit_all_negative_t():
    s = Sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(-1, s)
    xs = [i2, i1]
    i = Intersection.calculate_hit(xs)
    assert i == None

def test_hit_is_lowest_nonnegative_intersection():
    s = Sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = [i1, i2, i3, i4]
    i = Intersection.calculate_hit(xs)
    assert i == i4

def test_hit_is_lowest_nonnegative_intersection2():
    s = Sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(0, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = [i1, i2, i3, i4]
    i = Intersection.calculate_hit(xs)
    assert i == i2

def test_default_world_ray_intersection():
    w = DefaultWorld()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_world(r, w)
    assert len(xs) == 4
    assert is_approximately_equal(xs[0].t, 4)
    assert is_approximately_equal(xs[1].t, 4.5)
    assert is_approximately_equal(xs[2].t, 5.5)
    assert is_approximately_equal(xs[3].t, 6)

def test_precomputing_state_of_intersection():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    comp = i.prepare_computation(r)
    assert is_approximately_equal(comp.t, i.t)
    assert comp.object == i.object
    assert comp.point == Point(0, 0, -1)
    assert comp.eyev == Vector(0, 0, -1)
    assert comp.normalv == Vector(0, 0, -1)

def test_intersection_occurs_on_outside():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    comps = i.prepare_computation(r)
    assert not comps.inside

def test_intersection_occurs_on_inside():
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(1, shape)
    comps = i.prepare_computation(r)
    assert comps.point == Point(0, 0, 1)
    assert comps.eyev == Vector(0, 0, -1)
    assert comps.inside
    assert comps.normalv == Vector(0, 0, -1)

