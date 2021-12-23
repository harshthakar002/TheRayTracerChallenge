from features.point import Point
from features.vector import Vector
from figures.triangle import Triangle

def test_constructing_a_triange():
    p1 = Point(0, 1, 0)
    p2 = Point(-1, 0, 0)
    p3 = Point(1, 0, 0)
    t = Triangle(p1, p2, p3)
    assert t.p1 == p1
    assert t.p2 == p2
    assert t.p3 == p3
    assert t.e1 == Vector(-1, -1, 0)
    assert t.e2 == Vector(1, -1, 0)
    assert t.normal == Vector(0, 0, -1)