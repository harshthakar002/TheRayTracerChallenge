from patterns.ring_pattern import RingPattern
from features.point import Point
from features.color import WHITE_COLOR, BLACK_COLOR
from patterns.solid_pattern import SolidPattern
from figures.sphere import Sphere

def test_ring_should_extend_in_x_and_z():
    pattern = RingPattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    s = Sphere()
    assert pattern.color_at_object_point(s, Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at_object_point(s, Point(1, 0, 0)) == BLACK_COLOR
    assert pattern.color_at_object_point(s, Point(0, 0, 1)) == BLACK_COLOR
    assert pattern.color_at_object_point(s, Point(0.708, 0, 0.708)) == BLACK_COLOR