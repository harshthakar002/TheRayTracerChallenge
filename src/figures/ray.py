from __future__ import annotations
from features.point import Point
from features.vector import Vector
from matrix.matrix import Matrix

class Ray():

    def __init__(self, origin: Point, direction: Vector) -> None:
        self.origin = origin
        self.direction = direction

    def position(self, time: float) -> Point:
        return self.origin + (self.direction * time)

    def get_transformed_ray(self, origin_transformation: Matrix, direction_transformation: Matrix) -> Ray:
        new_origin = origin_transformation.multiply_matrix_and_tuple(self.origin)
        new_direction = direction_transformation.multiply_matrix_and_tuple(self.direction)
        return Ray(new_origin, new_direction)