from features.point import Point
from features.bounds import Bounds
from transformations.transformer import Transformer
from math import pi

def test_bounds_creation():
    b = Bounds(1, 2, 3, 4, 5, 6)
    assert b.min_point == Point(1, 2, 3)
    assert b.max_point == Point(4, 5, 6) 

def test_bounds_transform():
    b = Bounds(-1, -1, -1, 1, 1, 1)
    scaling = Transformer.scaling(1, 2, 1)
    rotation = Transformer.rotation_y(pi / 4)
    translation = Transformer.translation(2, 0 , 0)
    transformation = scaling.multiply_matrices(rotation).multiply_matrices(translation)
    new_b = b.transform(transformation)
    assert new_b == Bounds(0, -2, -2.82842, 2.82842, 2, 0)