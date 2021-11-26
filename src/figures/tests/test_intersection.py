from figures.intersection import Intersection
from figures.sphere import GlassSphere, Sphere
from features.equality import EPSILON, is_approximately_equal
from figures.ray import Ray
from features.point import Point
from features.vector import Vector
from transformations.figure_transformer import FigureTransformer
from physical.default_world import DefaultWorld
from figures.plane import Plane
from math import sqrt

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
    comp = i.prepare_computation(r, [i])
    assert is_approximately_equal(comp.t, i.t)
    assert comp.object == i.object
    assert comp.point == Point(0, 0, -1)
    assert comp.eyev == Vector(0, 0, -1)
    assert comp.normalv == Vector(0, 0, -1)

def test_intersection_occurs_on_outside():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    comps = i.prepare_computation(r, [i])
    assert not comps.inside

def test_intersection_occurs_on_inside():
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(1, shape)
    comps = i.prepare_computation(r, [i])
    assert comps.point == Point(0, 0, 1)
    assert comps.eyev == Vector(0, 0, -1)
    assert comps.inside
    assert comps.normalv == Vector(0, 0, -1)

def test_hit_should_offset_the_point():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = Sphere()
    shape.translation(0, 0, 1)
    i = Intersection(5, shape)
    comps = i.prepare_computation(r, [i])
    assert comps.over_point.z < -EPSILON / 2
    assert comps.point.z > comps.over_point.z

def test_refractive_index_calculations_in_computations():
    a = GlassSphere()
    a.scaling(2, 2, 2)
    a.material.refractive_index = 1.5
    b = GlassSphere()
    b.translation(0, 0, -0.25)
    b.material.refractive_index = 2.0
    c = GlassSphere()
    c.translation(0, 0, 0.25)
    c.material.refractive_index = 2.5
    r = Ray(Point(0, 0, -4), Vector(0, 0, 1))
    xs = [Intersection(2, a), Intersection(2.75, b), Intersection(3.25, c), Intersection(4.75, b), Intersection(5.25, c), Intersection(6, a)]
    comps = xs[0].prepare_computation(r, xs)
    assert is_approximately_equal(comps.n1, 1.0)
    assert is_approximately_equal(comps.n2, 1.5)
    comps = xs[1].prepare_computation(r, xs)
    assert is_approximately_equal(comps.n1, 1.5)
    assert is_approximately_equal(comps.n2, 2.0)
    comps = xs[2].prepare_computation(r, xs)
    assert is_approximately_equal(comps.n1, 2.0)
    assert is_approximately_equal(comps.n2, 2.5)
    comps = xs[3].prepare_computation(r, xs)
    assert is_approximately_equal(comps.n1, 2.5)
    assert is_approximately_equal(comps.n2, 2.5)
    comps = xs[4].prepare_computation(r, xs)
    assert is_approximately_equal(comps.n1, 2.5)
    assert is_approximately_equal(comps.n2, 1.5)
    comps = xs[5].prepare_computation(r, xs)
    assert is_approximately_equal(comps.n1, 1.5)
    assert is_approximately_equal(comps.n2, 1.0)

def test_under_point_is_offset_below_the_surface():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = GlassSphere()
    shape.translation(0, 0, 1)
    i = Intersection(5, shape)
    xs = [i]
    comps = i.prepare_computation(r, xs)
    assert comps.under_point.z > EPSILON / 2
    assert comps.point.z < comps.under_point.z

def test_precompute_reflection_vector():
    shape = Plane()
    r = Ray(Point(0, 1, -1), Vector(0, -sqrt(2) / 2, sqrt(2) / 2))
    i = Intersection(sqrt(2), shape)
    comps = i.prepare_computation(r, [i])
    assert comps.reflectv == Vector(0, sqrt(2) / 2, sqrt(2) / 2)

def test_schlick_approximation_under_total_internal_reflection():
    shape = GlassSphere()
    r = Ray(Point(0, 0, sqrt(2) / 2), Vector(0, 1, 0))
    xs = [Intersection(-sqrt(2) / 2, shape), Intersection(sqrt(2) / 2, shape)]
    comps = xs[1].prepare_computation(r, xs)
    reflectance = comps.schlick()
    assert is_approximately_equal(reflectance, 1.0)

def test_schlick_approximation_with_a_perpendicular_viewing_angle():
    shape = GlassSphere()
    r = Ray(Point(0, 0, 0), Vector(0, 1, 0))
    xs = [Intersection(-1, shape), Intersection(1, shape)]
    comps = xs[1].prepare_computation(r, xs)
    reflectance = comps.schlick()
    assert is_approximately_equal(reflectance, 0.04)

def test_schlick_approximation_with_small_angle_and_n2_greather_than_n1():
    shape = GlassSphere()
    r = Ray(Point(0, 0.99, -2), Vector(0, 0, 1))
    xs = [Intersection(1.8589, shape)]
    comps = xs[0].prepare_computation(r, xs)
    reflectance = comps.schlick()
    assert is_approximately_equal(reflectance, 0.48873)