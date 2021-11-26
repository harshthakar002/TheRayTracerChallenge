from patterns.stripe_pattern import StripePattern
from features.color import WHITE_COLOR, BLACK_COLOR
from features.point import Point
from figures.sphere import Sphere
from transformations.figure_transformer import FigureTransformer
from transformations.transformer import Transformer
from patterns.solid_pattern import SolidPattern
from figures.sphere import Sphere

def test_create_a_stripe_pattern():
    pattern = StripePattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    assert pattern.pattern1.color == WHITE_COLOR
    assert pattern.pattern2.color == BLACK_COLOR

def test_stripe_pattern_is_constant_in_y():
    pattern = StripePattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    s = Sphere()
    assert pattern.color_at_object_point(s, Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at_object_point(s, Point(0, 1, 0)) == WHITE_COLOR
    assert pattern.color_at_object_point(s, Point(0, 2, 0)) == WHITE_COLOR

def test_stripe_pattern_is_constant_in_z():
    pattern = StripePattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    s = Sphere()
    assert pattern.color_at_object_point(s, Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at_object_point(s, Point(0, 0, 1)) == WHITE_COLOR
    assert pattern.color_at_object_point(s, Point(0, 0, 2)) == WHITE_COLOR

def test_stripe_pattern_alternates_in_x():
    pattern = StripePattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    s = Sphere()
    assert pattern.color_at_object_point(s, Point(0, 0, 0)) == WHITE_COLOR
    assert pattern.color_at_object_point(s, Point(0.9, 0, 1)) == WHITE_COLOR
    assert pattern.color_at_object_point(s, Point(1, 0, 0)) == BLACK_COLOR
    assert pattern.color_at_object_point(s, Point(-0.1, 0, 0)) == BLACK_COLOR
    assert pattern.color_at_object_point(s, Point(-1, 0, 0)) == BLACK_COLOR
    assert pattern.color_at_object_point(s, Point(-1.1, 0, 0)) == WHITE_COLOR

def test_stripes_with_object_transformation():
    object = Sphere()
    object.scaling(2, 2, 2)
    pattern = StripePattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    c = pattern.color_at_object_point(object, Point(1.5, 0, 0))
    assert c == WHITE_COLOR

def test_stripes_with_pattern_transformation():
    object = Sphere()
    pattern = StripePattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    pattern_transform = Transformer.scaling(2, 2, 2)
    pattern.set_transform(pattern_transform)
    c = pattern.color_at_object_point(object, Point(1.5, 0, 0))
    assert c == WHITE_COLOR

def test_stripes_with_both_object_and_pattern_transformation():
    object = Sphere()
    pattern = StripePattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    object.scaling(2, 2, 2)
    pattern.translation(0.5, 0, 0)
    c = pattern.color_at_object_point(object, Point(2.5, 0, 0))
    assert c == WHITE_COLOR