from features.point import Point
from features.bounds import Bounds

def test_bounds_creation():
    b = Bounds(1, 2, 3, 4, 5, 6)
    assert b.min_point == Point(1, 2, 3)
    assert b.max_point == Point(4, 5, 6) 