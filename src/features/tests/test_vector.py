from features.tuple import Tuple
from features.vector import Vector, ZERO_VECTOR
from features.equality import is_approximately_equal
from math import sqrt

def test_vector_creation():
    v = Vector(4.0, -4.0, 3.0)
    assert v == Tuple(4.0, -4.0, 3.0, 0.0)
    assert v.is_vector()
    assert not v.is_point()

def test_subtract_two_vectors():
    v1 = Vector(3, 2, 1)
    v2 = Vector(5, 6, 7)
    difference = v1 - v2
    assert difference.is_vector()
    assert not difference.is_point()
    assert difference == Vector(-2, -4, -6)

def test_subtract_from_zero():
    v = Vector(1, -2, 3)
    difference = ZERO_VECTOR - v
    assert difference == Vector(-1, 2, -3)

def test_magnitude():
    v = Vector(1, 0, 0)
    assert is_approximately_equal(v.magnitude(), 1)
    v = Vector(0, 1, 0)
    assert is_approximately_equal(v.magnitude(), 1)
    v = Vector(0, 0, 1)
    assert is_approximately_equal(v.magnitude(), 1)
    v = Vector(1, 2, 3)
    assert is_approximately_equal(v.magnitude(), sqrt(14))
    v = Vector(-1, -2, -3)
    assert is_approximately_equal(v.magnitude(), sqrt(14))

def test_normalize():
    v = Vector(4, 0, 0)
    assert v.normalize() == Vector(1, 0, 0)
    assert v.normalize().magnitude() == 1
    v = Vector(1, 2, 3)
    assert v.normalize() == Vector(0.26726, 0.53452, 0.80178)
    assert v.normalize().magnitude() == 1

def test_dot_product():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert a.dotProduct(b) == 20


def test_cross_product():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert a.crossProduct(b) == Vector(-1, 2, -1)
    assert b.crossProduct(a) == Vector(1, -2, 1)

def test_reflection_on_a_normal_surface():
    v = Vector(1, -1, 0)
    n = Vector(0, 1, 0)
    r = v.reflect(n)
    assert r == Vector(1, 1, 0)

def test_reflection_off_a_slanted_surface():
    v = Vector(0, -1, 0)
    n = Vector(sqrt(2) / 2, sqrt(2) / 2, 0)
    r = v.reflect(n)
    assert r == Vector(1, 0, 0)