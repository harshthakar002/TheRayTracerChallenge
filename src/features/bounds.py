from __future__ import annotations
from typing import List
from features.point import Point
from features.tuple import Tuple
from matrix.matrix import Matrix
from math import inf

class Bounds():

    def __init__(self, min_x: float, min_y: float, min_z: float, max_x: float, max_y: float, max_z: float) -> None:
        if min_x > max_x or min_y > max_y or min_z > max_z:
            raise ValueError('min value cannpt be greater than max value')
        self.min_point = Point(min_x, min_y, min_z)
        self.max_point = Point(max_x, max_y, max_z)
    
    def __eq__(self, bounds: Bounds) -> bool:
        return self.min_point == bounds.min_point and self.max_point == bounds.max_point
    
    def transform(self, transformation_matrix: Matrix) -> Bounds:
        transformed_vertices: List[Tuple] = []
        ## we need to trandform each point of the cube individually and find a bounding box of the new transofrmed cube
        transformed_vertices.append(transformation_matrix.multiply_matrix_and_tuple(Point(self.min_point.x, self.min_point.y, self.min_point.z)))
        transformed_vertices.append(transformation_matrix.multiply_matrix_and_tuple(Point(self.min_point.x, self.min_point.y, self.max_point.z)))
        transformed_vertices.append(transformation_matrix.multiply_matrix_and_tuple(Point(self.min_point.x, self.max_point.y, self.min_point.z)))
        transformed_vertices.append(transformation_matrix.multiply_matrix_and_tuple(Point(self.min_point.x, self.max_point.y, self.max_point.z)))
        transformed_vertices.append(transformation_matrix.multiply_matrix_and_tuple(Point(self.max_point.x, self.min_point.y, self.min_point.z)))
        transformed_vertices.append(transformation_matrix.multiply_matrix_and_tuple(Point(self.max_point.x, self.min_point.y, self.max_point.z)))
        transformed_vertices.append(transformation_matrix.multiply_matrix_and_tuple(Point(self.max_point.x, self.max_point.y, self.min_point.z)))
        transformed_vertices.append(transformation_matrix.multiply_matrix_and_tuple(Point(self.max_point.x, self.max_point.y, self.max_point.z)))
        min_x, min_y, min_z = inf, inf, inf
        max_x, max_y, max_z = -inf, -inf, -inf
        for transformed_vertex in transformed_vertices:
            min_x = min(min_x, transformed_vertex.x)
            min_y = min(min_y, transformed_vertex.y)
            min_z = min(min_z, transformed_vertex.z)
            max_x = max(max_x, transformed_vertex.x)
            max_y = max(max_y, transformed_vertex.y)
            max_z = max(max_z, transformed_vertex.z)
        return Bounds(min_x, min_y, min_z, max_x, max_y, max_z)
    
    @staticmethod
    def find_bounds_of_group_of_bounds(bounds_list: List[Bounds]) -> Bounds:
        if len(bounds_list) == 0:
            return Bounds(0, 0, 0, 0, 0, 0)
        min_x, min_y, min_z = inf, inf, inf
        max_x, max_y, max_z = -inf, -inf, -inf
        for bounds in bounds_list:
            min_x = min(min_x, bounds.min_point.x)
            min_y = min(min_y, bounds.min_point.y)
            min_z = min(min_z, bounds.min_point.z)
            max_x = max(max_x, bounds.max_point.x)
            max_y = max(max_y, bounds.max_point.y)
            max_z = max(max_z, bounds.max_point.z)
        return Bounds(min_x, min_y, min_z, max_x, max_y, max_z)