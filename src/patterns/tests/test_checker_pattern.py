from patterns.checker_pattern import CheckerPattern
from features.color import WHITE_COLOR, BLACK_COLOR
from features.point import Point
from patterns.solid_pattern import SolidPattern

def test_checkers_should_repeat_in_x():
    pattern = CheckerPattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    assert pattern.color_at(Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0.99, 0, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(1.01, 0, 0)) == BLACK_COLOR

def test_checkers_should_repeat_in_y():
    pattern = CheckerPattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    assert pattern.color_at(Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 0.99, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 1.01, 0)) == BLACK_COLOR

def test_checkers_should_repeat_in_z():
    pattern = CheckerPattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    assert pattern.color_at(Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 0, 0.99)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 0, 1.01)) == BLACK_COLOR