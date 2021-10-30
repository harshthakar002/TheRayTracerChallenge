from features.point import Point
from features.vector import Vector
from matrix.matrix import Matrix
from transformations.transformer import Transformer

class ViewTransformer():

    @staticmethod
    def view_transform(from_point: Point, to_point: Point, up: Vector) -> Matrix:
        forward = Vector.fromtuple(to_point - from_point).normalize()
        left = forward.crossProduct(up.normalize())
        true_up = left.crossProduct(forward)
        orientation = Matrix.initialize_from_values([[left.x, left.y, left.z, 0], 
        [true_up.x, true_up.y, true_up.z, 0], [-forward.x, -forward.y, -forward.z, 0], 
        [0, 0, 0, 1]])
        return orientation.multiply_matrices(Transformer.translation(-from_point.x, -from_point.y, -from_point.z))