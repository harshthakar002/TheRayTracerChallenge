from features.tuple import tuple
from features.point import point
from features.vector import vector

def test_point_creation():
    p = point(4.0, -4.0, 3.0)
    assert p == tuple(4.0, -4.0, 3.0, 1.0)
    assert not p.is_vector()
    assert p.is_point()

def test_subtract_two_points():
    p1 = point(3, 2, 1)
    p2 = point(5, 6, 7)
    difference = p1 - p2
    assert difference.is_vector()
    assert not difference.is_point()
    assert difference == vector(-2, -4, -6)

def test_subtract_vector_from_point():
    p = point(3, 2, 1)
    v = vector(5, 6, 7)
    difference = p - v
    assert difference.is_point()
    assert not difference.is_vector()
    assert difference == point(-2, -4, -6)