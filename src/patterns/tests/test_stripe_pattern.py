from patterns.stripe_pattern import StripePattern
from features.color import WHITE_COLOR, BLACK_COLOR
from features.point import Point
from figures.sphere import Sphere
from transformations.figure_transformer import FigureTransformer
from transformations.transformer import Transformer

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

def test_stripes_with_object_transformation():
    object = Sphere()
    object_transform, direction_transform = FigureTransformer.scaling(2, 2, 2)
    object.set_transform(object_transform, direction_transform)
    pattern = StripePattern(WHITE_COLOR, BLACK_COLOR)
    c = pattern.color_at_object_point(object, Point(1.5, 0, 0))
    assert c == WHITE_COLOR

def test_stripes_with_pattern_transformation():
    object = Sphere()
    pattern = StripePattern(WHITE_COLOR, BLACK_COLOR)
    pattern_transform = Transformer.scaling(2, 2, 2)
    pattern.set_transform(pattern_transform)
    c = pattern.color_at_object_point(object, Point(1.5, 0, 0))
    assert c == WHITE_COLOR

def test_stripes_with_both_object_and_pattern_transformation():
    object = Sphere()
    pattern = StripePattern(WHITE_COLOR, BLACK_COLOR)
    object_transform, direction_transform = FigureTransformer.scaling(2, 2, 2)
    object.set_transform(object_transform, direction_transform)
    pattern_object_transform = Transformer.translation(0.5, 0, 0)
    pattern.set_transform(pattern_object_transform)
    c = pattern.color_at_object_point(object, Point(2.5, 0, 0))
    assert c == WHITE_COLOR