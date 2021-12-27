from typing import List, Tuple
from features.bounds import Bounds
from features.equality import EPSILON
from features.point import Point
from features.vector import Vector
from figures.ray import Ray
from figures.shape import Shape
from math import inf

class Group(Shape):

    def __init__(self, name: str = 'DefaultGroup') -> None:
        super().__init__()
        self.shapes: List[Shape] = []
        self.memoized_bounds = Bounds(0, 0, 0, 0, 0, 0)
        self.name = name

    def is_empty(self) -> bool:
        return len(self.shapes) == 0
    
    def contains(self, shape: Shape) -> bool:
        return shape in self.shapes

    def add_child(self, shape: Shape) -> None:
        self.shapes.append(shape)
        shape.parent = self
        if len(self.shapes) > 1:
            self.memoized_bounds = Bounds.find_bounds_of_group_of_bounds([shape.bounds().transform(shape.transform), self.memoized_bounds])
        else:
            self.memoize_bounds()
        if self.parent != None:
            self.parent.memoize_bounds()
    
    def local_intersect(self, ray: Ray) -> List[tuple[float, Shape]]:
        transformed_ray = ray.get_transformed_ray(self.ray_transform)
        if self.is_out_of_bounds(transformed_ray):
            return []
        
        intersection_distances_and_shapes: List[tuple[float, Shape]] = []
        for shape in self.shapes:
            intersection_distances_and_shapes += shape.local_intersect(transformed_ray)
        return sorted(intersection_distances_and_shapes, key=lambda intersection_distance_and_shape: intersection_distance_and_shape[0])
    
    def normal_at(self, point: Point) -> Vector:
        raise NotImplementedError('This method should not be called for groups')
    
    def bounds(self) -> Bounds:
        return self.memoized_bounds
        
    def get_bounds_for_shapes(self) -> List[Bounds]:
        bounds_list : List[Bounds] = []
        for shape in self.shapes:
            bounds_list.append(shape.bounds().transform(shape.transform))
        return bounds_list

    def is_out_of_bounds(self, ray: Ray) -> bool:
        bounds = self.bounds()
        xtmin, xtmax = Group.check_axis(bounds.min_point.x, bounds.max_point.x, ray.origin.x, ray.direction.x)
        ytmin, ytmax = Group.check_axis(bounds.min_point.y, bounds.max_point.y, ray.origin.y, ray.direction.y)
        ztmin, ztmax = Group.check_axis(bounds.min_point.z, bounds.max_point.z, ray.origin.z, ray.direction.z)
        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)
        return tmin > tmax

    @staticmethod
    def check_axis(min_value: float, max_value: float, origin: float, direction:float) -> Tuple[float, float]:
        tmin_numerator = min_value - origin
        tmax_numerator = max_value - origin
        if abs(direction) >= EPSILON:
            tmin = tmin_numerator / direction
            tmax = tmax_numerator / direction
        else:
            tmin = tmin_numerator * inf
            tmax = tmax_numerator * inf
        
        if tmin > tmax:
            tmin, tmax = tmax, tmin
        return tmin, tmax
    
    def memoize_bounds(self) -> None:
        self.memoized_bounds = Bounds.find_bounds_of_group_of_bounds(self.get_bounds_for_shapes())

    def optimise_by_splitting_by_n(self, n: int) -> None:
        n = 7
        bounds = self.bounds()
        delta = bounds.max_point - bounds.min_point
        mat: list[list[list[Group]]] = []
        for i in range(n):
            mat.append([])
            for j in range(n):
                mat[i].append([])
                for k in range(n):
                    mat[i][j].append(Group(self.name + '_Group' + str(i) + str(j) + str(k)))
        dx, dy, dz = delta.x / n, delta.y / n, delta.z / n
        for shape in self.shapes:
            s_bounds: Bounds = shape.bounds()
            s_mid = (s_bounds.max_point + s_bounds.min_point) / 2
            mat[int(s_mid.x / dx)][int(s_mid.y / dy)][int(s_mid.z / dz)].add_child(shape)
        self.shapes = []
        self.memoize_bounds()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if len(mat[i][j][k].shapes) != 0:
                        self.add_child(mat[i][j][k])