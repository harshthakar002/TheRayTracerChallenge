from features.tuple import tuple
from features.vector import vector, ZERO_VECTOR
from features.equality import isApproximatelyEqual
import math

def test_vector_creation():
    v = vector(4.0, -4.0, 3.0)
    assert v == tuple(4.0, -4.0, 3.0, 0.0)
    assert v.isVector()
    assert not v.isPoint()

def test_subtract_two_vectors():
    v1 = vector(3, 2, 1)
    v2 = vector(5, 6, 7)
    difference = v1 - v2
    assert difference.isVector()
    assert not difference.isPoint()
    assert difference == vector(-2, -4, -6)

def test_subtract_from_zero():
    v = vector(1, -2, 3)
    difference = ZERO_VECTOR - v
    assert difference == vector(-1, 2, -3)

def test_magnitude():
    v = vector(1, 0, 0)
    assert isApproximatelyEqual(v.magnitude(), 1)
    v = vector(0, 1, 0)
    assert isApproximatelyEqual(v.magnitude(), 1)
    v = vector(0, 0, 1)
    assert isApproximatelyEqual(v.magnitude(), 1)
    v = vector(1, 2, 3)
    assert isApproximatelyEqual(v.magnitude(), math.sqrt(14))
    v = vector(-1, -2, -3)
    assert isApproximatelyEqual(v.magnitude(), math.sqrt(14))

def test_normalize():
    v = vector(4, 0, 0)
    assert v.normalize() == vector(1, 0, 0)
    assert v.normalize().magnitude() == 1
    v = vector(1, 2, 3)
    assert v.normalize() == vector(0.26726, 0.53452, 0.80178)
    assert v.normalize().magnitude() == 1
