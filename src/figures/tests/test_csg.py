from figures.csg import CSG, CSGOperation
from figures.cube import Cube
from figures.sphere import Sphere

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