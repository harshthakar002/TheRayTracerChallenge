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
        transformed_ray = ray.get_transformed_ray(self.ray_origin_transform, self.ray_direction_transform)
        return self.local_intersection_distance(transformed_ray)
    
    def normal_at(self, point: Point) -> Vector:
       object_point = self.ray_origin_transform.multiply_matrix_and_tuple(point)
       object_normal = self.local_normal_at(object_point)
       world_normal = self.ray_origin_transform.transposed_matrix().multiply_matrix_and_tuple(object_normal)
       return Vector(world_normal.x, world_normal.y, world_normal.z).normalize() 
    
    def set_transform(self, origin_transform: Matrix, direction_transform: Matrix) -> None:
        self.origin_transform = self.origin_transform.multiply_matrices(origin_transform)
        self.direction_transform = self.direction_transform.multiply_matrices(direction_transform)
        self.ray_origin_transform = MatrixInverter.invert(self.origin_transform)
        self.ray_direction_transform = MatrixInverter.invert(self.direction_transform)
    
    def local_intersection_distance(self, ray: Ray) -> List[float]:
        raise NotImplementedError('Abstract method')

    def local_normal_at(self, point: Point) -> Vector:
        raise NotImplementedError('Abstract Method')
