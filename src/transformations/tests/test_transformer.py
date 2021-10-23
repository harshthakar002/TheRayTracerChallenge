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

def test_point_scaling():
    transform = Transformer.scaling(2, 3, -4)
    p = Point(-4, 6, 8)
    assert transform.multiply_matrix_and_tuple(p) == Point(-8, 18, -32)

def test_vector_scaling():
    transform = Transformer.scaling(2, 3, 4)
    v = Vector(-4, 6, 8)
    assert transform.multiply_matrix_and_tuple(v) == Vector(-8, 18, 32)

def test_vector_inverse_scaling():
    transform = Transformer.scaling(2, 3, 4)
    inverse_transform = MatrixInverter.invert(transform)
    v = Vector(-4, 6, 8)
    assert inverse_transform.multiply_matrix_and_tuple(v) == Vector(-2, 2, 2)