from features.tuple import tuple
from features.point import point

def test_point_creation():
    p = point(4.0, -4.0, 3.0)
    assert p.equals(tuple(4.0, -4.0, 3.0, 1.0))
    assert not p.isVector()
    assert p.isPoint()