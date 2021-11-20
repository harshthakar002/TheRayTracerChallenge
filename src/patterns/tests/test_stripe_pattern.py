from patterns.stripe_pattern import StripePattern
from features.color import WHITE_COLOR, BLACK_COLOR
from features.point import Point

def test_create_a_stripe_pattern():
    pattern = StripePattern(WHITE_COLOR, BLACK_COLOR)
    assert pattern.color1 == WHITE_COLOR
    assert pattern.color2 == BLACK_COLOR

def test_stripe_pattern_is_constant_in_y():
    pattern = StripePattern(WHITE_COLOR, BLACK_COLOR)
    assert pattern.color_at(Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 1, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 2, 0)) == WHITE_COLOR

def test_stripe_pattern_is_constant_in_z():
    pattern = StripePattern(WHITE_COLOR, BLACK_COLOR)
    assert pattern.color_at(Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 0, 1)) == WHITE_COLOR
    assert pattern.color_at(Point(0, 0, 2)) == WHITE_COLOR

def test_stripe_pattern_alternates_in_x():
    pattern = StripePattern(WHITE_COLOR, BLACK_COLOR)
    assert pattern.color_at(Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at(Point(0.9, 0, 1)) == WHITE_COLOR
    assert pattern.color_at(Point(1, 0, 0)) == BLACK_COLOR
    assert pattern.color_at(Point(-0.1, 0, 0)) == BLACK_COLOR
    assert pattern.color_at(Point(-1, 0, 0)) == BLACK_COLOR
    assert pattern.color_at(Point(-1.1, 0, 0)) == WHITE_COLOR