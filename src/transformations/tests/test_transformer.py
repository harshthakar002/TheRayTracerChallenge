from matrix.matrix import Matrix
from transformations.transformer import Transformer
from features.vector import Vector
from features.point import Point
from matrix.matrix_inverter import MatrixInverter

def test_point_translation():
    transform = Transformer.translation(5, -3, 2)
    p = Point(-3, 4, 5)
    assert transform.multiply_matrix_and_tuple(p) == Point(2, 1, 7)

def test_point_inverse_translation():
    transform = Transformer.translation(5, -3, 2)
    inverse_transform = MatrixInverter.invert(transform)
    p = Point(-3, 4, 5)
    assert inverse_transform.multiply_matrix_and_tuple(p) == Point(-8, 7, 3)

def test_vector_translation():
    transform = Transformer.translation(5, -3, 2)
    v = Vector(-3, 4, 5)
    assert transform.multiply_matrix_and_tuple(v) == v