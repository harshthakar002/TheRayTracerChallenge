from patterns.solid_pattern import SolidPattern
from features.color import WHITE_COLOR
from features.point import Point

def test_solid_pattern():
    pattern = SolidPattern(WHITE_COLOR)
    assert pattern.color_at(Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 1, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 0, 1)) == WHITE_COLOR
    assert pattern.color_at(Point(1, 0, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(1, 1, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 1, 1)) == WHITE_COLOR
    assert pattern.color_at(Point(1, 0, 1)) == WHITE_COLOR