from features.tuple import tuple
from features.point import point

def test_point_creation():
    v = point(4.0, -4.0, 3.0)
    assert v.equals(tuple(4.0, -4.0, 3.0, 1.0))
    assert not v.isVector()
    assert v.isPoint()