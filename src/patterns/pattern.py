from features.color import Color
from features.point import Point
from figures.figure import Figure
from matrix.matrix import Matrix
from matrix.matrix_inverter import MatrixInverter
from transformations.transformable import Transformable

class Pattern(Transformable):

    def __init__(self) -> None:
        self.transform = Matrix.generate_identity_matrix(4)
        self.point_transform = Matrix.generate_identity_matrix(4)

    def color_at(self, point: Point) -> Color:
        raise NotImplementedError('Not implemented for base class')

    def set_transform(self, transform: Matrix) -> None:
        self.point_transform = self.point_transform.multiply_matrices(transform)
        self.transform = MatrixInverter.invert(self.point_transform)

    def color_at_object_point(self, object: Figure, point: Point):
        object_point = object.ray_transform.multiply_matrix_and_tuple(point)
        pattern_point = self.transform.multiply_matrix_and_tuple(object_point)
        return self.color_at(pattern_point)