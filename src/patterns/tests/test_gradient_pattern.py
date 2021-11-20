from patterns.gradient_pattern import GradientPattern
from features.color import Color, WHITE_COLOR, BLACK_COLOR
from features.point import Point
from patterns.solid_pattern import SolidPattern

def test_gradient_pattern():
    pattern = GradientPattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    assert pattern.color_at(Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0.25, 0, 0)) == Color(0.75, 0.75, 0.75)
    assert pattern.color_at(Point(0.5, 0, 0)) == Color(0.5, 0.5, 0.5)
    assert pattern.color_at(Point(0.75, 0, 0)) == Color(0.25, 0.25, 0.25)