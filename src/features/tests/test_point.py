from features.tuple import Tuple
from features.point import Point
from features.vector import Vector

def test_point_creation():
    p = Point(4.0, -4.0, 3.0)
    assert p == Tuple(4.0, -4.0, 3.0, 1.0)
    assert not p.is_vector()
    assert p.is_point()

def test_subtract_two_points():
    p1 = Point(3, 2, 1)
    p2 = Point(5, 6, 7)
    difference = p1 - p2
    assert difference.is_vector()
    assert not difference.is_point()
    assert difference == Vector(-2, -4, -6)

def test_subtract_vector_from_point():
    p = Point(3, 2, 1)
    v = Vector(5, 6, 7)
    difference = p - v
    assert difference.is_point()
    assert not difference.is_vector()
    assert difference == Point(-2, -4, -6)