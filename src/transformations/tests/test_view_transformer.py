from transformations.view_transformer import ViewTransformer
from features.point import Point
from features.vector import Vector
from matrix.matrix import Matrix
from transformations.transformer import Transformer

def test_default_orientation_matrix():
    from_point = Point(0, 0, 0)
    to_point = Point(0, 0, -1)
    up = Vector(0, 1, 0)
    t = ViewTransformer.view_transform(from_point, to_point, up)
    assert t == Matrix.generate_identity_matrix(4)

def test_view_transformation_positive_z_direction():
    from_point = Point(0, 0, 0)
    to_point = Point(0, 0, 1)
    up = Vector(0, 1, 0)
    t = ViewTransformer.view_transform(from_point, to_point, up)
    assert t == Transformer.scaling(-1, 1, -1)

def test_view_transformation_moves_world():
    from_point = Point(0, 0, 8)
    to_point = Point(0, 0, 0)
    up = Vector(0, 1, 0)
    t = ViewTransformer.view_transform(from_point, to_point, up)
    assert t == Transformer.translation(0, 0, -8)

def test_arbitrary_view_transformation():
    from_point = Point(1, 3, 2)
    to_point = Point(4, -2, 8)
    up = Vector(1, 1, 0)
    t = ViewTransformer.view_transform(from_point, to_point, up)
    assert t == Matrix.initialize_from_values([
    [-0.50709, 0.50709,  0.67612, -2.36643],
    [0.76772, 0.60609, 0.12122, -2.82843],
    [-0.35857, 0.59761, -0.71714, 0],
    [0, 0, 0, 1]])