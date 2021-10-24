from uuid import uuid4
from figures.ray import Ray
from typing import List
from matrix.matrix import Matrix
from matrix.matrix_inverter import MatrixInverter
from features.point import Point
from features.vector import Vector
from physical.material import Material

class Figure():

    def __init__(self):
        self.id = uuid4().int
        self.origin_transform = Matrix.generate_identity_matrix(4)
        self.ray_origin_transform = Matrix.generate_identity_matrix(4)
        self.direction_transform = Matrix.generate_identity_matrix(4)
        self.ray_direction_transform = Matrix.generate_identity_matrix(4)
        self.material = Material()
    
    def ray_intersection_distance(self, ray: Ray) -> List[float]:
        raise NotImplementedError('Abstract method')
    
    def normal_at(self, point: Point) -> Vector:
        raise NotImplementedError('Abstract Method')
    
    def set_transform(self, origin_transform: Matrix, direction_transform: Matrix) -> None:
        self.origin_transform = self.origin_transform.multiply_matrices(origin_transform)
        self.direction_transform = self.direction_transform.multiply_matrices(direction_transform)
        self.ray_origin_transform = MatrixInverter.invert(self.origin_transform)
        self.ray_direction_transform = MatrixInverter.invert(self.direction_transform)