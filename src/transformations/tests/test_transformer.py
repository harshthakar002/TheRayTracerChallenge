from transformations.transformer import Transformer
from features.vector import Vector
from features.point import Point
from matrix.matrix_inverter import MatrixInverter
from math import sqrt, pi

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

def test_point_reflection():
    transform = Transformer.scaling(-1, 1, 1)
    p = Point(2, 3, 4)
    assert transform.multiply_matrix_and_tuple(p) == Point(-2, 3, 4)

def test_rotation_x():
    p = Point(0, 1, 0)
    half_quarter = Transformer.rotation_x(pi / 4)
    full_quarter = Transformer.rotation_x(pi / 2)
    assert half_quarter.multiply_matrix_and_tuple(p) == Point(0, sqrt(2) / 2, sqrt(2) / 2)
    assert full_quarter.multiply_matrix_and_tuple(p) == Point(0, 0, 1)

def test_inverse_rotation_x():
    p = Point(0, 1, 0)
    half_quarter = Transformer.rotation_x(pi / 4)
    inverse_transform = MatrixInverter.invert(half_quarter)
    assert inverse_transform.multiply_matrix_and_tuple(p) == Point(0, sqrt(2) / 2, (-sqrt(2)) / 2)

def test_rotation_y():
    p = Point(0, 0, 1)
    half_quarter = Transformer.rotation_y(pi / 4)
    full_quarter = Transformer.rotation_y(pi / 2)
    assert half_quarter.multiply_matrix_and_tuple(p) == Point(sqrt(2) / 2, 0, sqrt(2) / 2)
    assert full_quarter.multiply_matrix_and_tuple(p) == Point(1, 0, 0)
    
def test_rotation_z():
    p = Point(0, 1, 0)
    half_quarter = Transformer.rotation_z(pi / 4)
    full_quarter = Transformer.rotation_z(pi / 2)
    assert half_quarter.multiply_matrix_and_tuple(p) == Point((-sqrt(2)) / 2, sqrt(2) / 2, 0)
    assert full_quarter.multiply_matrix_and_tuple(p) == Point(-1, 0, 0)

def test_shearing_xy():
    p = Point(2, 3, 4)
    transform = Transformer.shearing(1, 0, 0, 0, 0, 0)
    assert transform.multiply_matrix_and_tuple(p) == Point(5, 3, 4)

def test_shearing_xz():
    p = Point(2, 3, 4)
    transform = Transformer.shearing(0, 1, 0, 0, 0, 0)
    assert transform.multiply_matrix_and_tuple(p) == Point(6, 3, 4)

def test_shearing_yx():
    p = Point(2, 3, 4)
    transform = Transformer.shearing(0, 0, 1, 0, 0, 0)
    assert transform.multiply_matrix_and_tuple(p) == Point(2, 5, 4)

def test_shearing_yz():
    p = Point(2, 3, 4)
    transform = Transformer.shearing(0, 0, 0, 1, 0, 0)
    assert transform.multiply_matrix_and_tuple(p) == Point(2, 7, 4)

def test_shearing_zx():
    p = Point(2, 3, 4)
    transform = Transformer.shearing(0, 0, 0, 0, 1, 0)
    assert transform.multiply_matrix_and_tuple(p) == Point(2, 3, 6)

def test_shearing_zy():
    p = Point(2, 3, 4)
    transform = Transformer.shearing(0, 0, 0, 0, 0, 1)
    assert transform.multiply_matrix_and_tuple(p) == Point(2, 3, 7)