from __future__ import annotations
from uuid import uuid4
from figures.ray import Ray
from typing import List
from matrix.matrix import Matrix
from matrix.matrix_inverter import MatrixInverter
from features.point import Point
from features.vector import Vector
from physical.material import Material
from transformations.transformable import Transformable

class Shape(Transformable):

    def __init__(self):
        self.id = uuid4().int
        self.transform = Matrix.generate_identity_matrix(4)
        self.ray_transform = Matrix.generate_identity_matrix(4)
        self.material = Material()
        self.parent = None
    
    def normal_at(self, point: Point) -> Vector:
       object_point = self.ray_transform.multiply_matrix_and_tuple(point)
       object_normal = self.local_normal_at(object_point)
       world_normal = self.ray_transform.transposed_matrix().multiply_matrix_and_tuple(object_normal)
       return Vector(world_normal.x, world_normal.y, world_normal.z).normalize() 
    
    def set_transform(self, transform: Matrix) -> None:
        self.transform = self.transform.multiply_matrices(transform)
        self.ray_transform = MatrixInverter.invert(self.transform)
    
    def local_intersection_distance(self, ray: Ray) -> List[float]:
        raise NotImplementedError('Abstract method')

    def local_normal_at(self, point: Point) -> Vector:
        raise NotImplementedError('Abstract Method')

    def local_intersect(self, ray: Ray) -> List[tuple[float, Shape]]:
        transformed_ray = ray.get_transformed_ray(self.ray_transform)
        intersection_distances = self.local_intersection_distance(transformed_ray)
        intersections = []
        for intersection_distance in intersection_distances:
            intersections.append((intersection_distance, self))
        return intersections

    def world_to_object(self, point: Point) -> Point:
        if self.parent != None:
            point = self.parent.world_to_object(point)
        
        return Point.fromTuple(MatrixInverter.invert(self.transform).multiply_matrix_and_tuple(point))
    
    def normal_to_world(self, normal: Vector) -> Vector:
        normal = MatrixInverter.invert(self.transform).transposed_matrix().multiply_matrix_and_tuple(normal)
        normal.w = 0
        normal = Vector.fromtuple(normal).normalize()

        if self.parent != None:
            normal = self.parent.normal_to_world(normal)
        
        return normal