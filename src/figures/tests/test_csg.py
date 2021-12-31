from figures.csg import CSG, CSGOperation
from figures.cube import Cube
from figures.sphere import Sphere
from features.point import Point
from features.vector import Vector
from figures.ray import Ray
from features.equality import is_approximately_equal

def test_csg_construction():
    s1 = Sphere()
    s2 = Cube()
    c = CSG(CSGOperation.UNION, s1, s2)
    assert c.operation == CSGOperation.UNION
    assert c.left == s1
    assert c.right == s2
    assert s1.parent == c
    assert s2.parent == c

def test_csg_intersection_allowed():
    assert not CSG.is_intersection_allowed(CSGOperation.UNION, True, True, True)
    assert CSG.is_intersection_allowed(CSGOperation.UNION, True, True, False)
    assert not CSG.is_intersection_allowed(CSGOperation.UNION, True, False, True)
    assert CSG.is_intersection_allowed(CSGOperation.UNION, True, False, False)
    assert not CSG.is_intersection_allowed(CSGOperation.UNION, False, True, True)
    assert not CSG.is_intersection_allowed(CSGOperation.UNION, False, True, False)
    assert CSG.is_intersection_allowed(CSGOperation.UNION, False, False, True)
    assert CSG.is_intersection_allowed(CSGOperation.UNION, False, False, False)
    assert CSG.is_intersection_allowed(CSGOperation.INTERSECTION, True, True, True)
    assert not CSG.is_intersection_allowed(CSGOperation.INTERSECTION, True, True, False)
    assert CSG.is_intersection_allowed(CSGOperation.INTERSECTION, True, False, True)
    assert not CSG.is_intersection_allowed(CSGOperation.INTERSECTION, True, False, False)
    assert CSG.is_intersection_allowed(CSGOperation.INTERSECTION, False, True, True)
    assert CSG.is_intersection_allowed(CSGOperation.INTERSECTION, False, True, False)
    assert not CSG.is_intersection_allowed(CSGOperation.INTERSECTION, False, False, True)
    assert not CSG.is_intersection_allowed(CSGOperation.INTERSECTION, False, False, False)
    assert not CSG.is_intersection_allowed(CSGOperation.DIFFERENCE, True, True, True)
    assert CSG.is_intersection_allowed(CSGOperation.DIFFERENCE, True, True, False)
    assert not CSG.is_intersection_allowed(CSGOperation.DIFFERENCE, True, False, True)
    assert CSG.is_intersection_allowed(CSGOperation.DIFFERENCE, True, False, False)
    assert CSG.is_intersection_allowed(CSGOperation.DIFFERENCE, False, True, True)
    assert CSG.is_intersection_allowed(CSGOperation.DIFFERENCE, False, True, False)
    assert not CSG.is_intersection_allowed(CSGOperation.DIFFERENCE, False, False, True)
    assert not CSG.is_intersection_allowed(CSGOperation.DIFFERENCE, False, False, False)

def test_filtering_out_list_of_intersections():
    s1 = Sphere()
    s2 = Cube()
    c = CSG(CSGOperation.UNION, s1, s2)
    xs = [(1, s1, None, None), (2, s2, None, None), (3, s1, None, None), (4, s2, None, None)]
    result = c.filter_intersections(xs)
    assert len(result) == 2
    assert result[0] == xs[0]
    assert result[1] == xs[3]
    c = CSG(CSGOperation.INTERSECTION, s1, s2)
    result = c.filter_intersections(xs)
    assert len(result) == 2
    assert result[0] == xs[1]
    assert result[1] == xs[2]
    c = CSG(CSGOperation.DIFFERENCE, s1, s2)
    result = c.filter_intersections(xs)
    assert len(result) == 2
    assert result[0] == xs[0]
    assert result[1] == xs[1]

def test_ray_misses_csg():
    c = CSG(CSGOperation.UNION, Sphere(), Cube())
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
    xs = c.local_intersect(r)
    assert len(xs) == 0

def test_ray_hits_csg_object():
    s1 = Sphere()
    s2 = Sphere()
    s2.translation(0, 0, 0.5)
    c = CSG(CSGOperation.UNION, s1, s2)
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    xs = c.local_intersect(r)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0][0], 4)
    assert xs[0][1] == s1
    assert is_approximately_equal(xs[1][0], 6.5)
    assert xs[1][1] == s2