from features.tuple import tuple
from features.vector import vector

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