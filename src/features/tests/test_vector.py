from features.tuple import tuple
from features.vector import vector

def test_vector_creation():
    v = vector(4.0, -4.0, 3.0)
    assert v.equals(tuple(4.0, -4.0, 3.0, 0.0))
    assert v.isVector()
    assert not v.isPoint()