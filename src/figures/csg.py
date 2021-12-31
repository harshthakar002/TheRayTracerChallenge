from enum import Enum, unique
from typing import List
from features.bounds import Bounds
from features.point import Point
from features.vector import Vector
from figures.group import Group
from figures.ray import Ray
from figures.shape import Shape

@unique
class CSGOperation(Enum):
    UNION = 'UNION'
    INTERSECTION = 'INTERSECTION'
    DIFFERENCE = 'DIFFERENCE'


class CSG(Shape):

    def __init__(self, operation: CSGOperation, left: Shape, right: Shape):
        super().__init__()
        self.operation = operation
        self.left = left
        left.parent = self
        self.right = right
        right.parent = self
        self.memoized_bounds = Bounds.find_bounds_of_group_of_bounds([self.left.bounds(), self.right.bounds()])
    
    def filter_intersections(self, intersections: List[tuple[float, Shape, float, float]]):
        is_in_left, is_in_right = False, False
        result: List[tuple[float, Shape, float, float]] = []
        for intersection_distance, shape, u, v in intersections:
            is_left_hit = self.left.is_equal_to_shape_or_is_child_shape(shape)
            if CSG.is_intersection_allowed(self.operation, is_left_hit, is_in_left, is_in_right):
                result.append((intersection_distance, shape, u, v))
            if is_left_hit:
                is_in_left = not is_in_left
            else:
                is_in_right = not is_in_right
        return result

    def is_equal_to_shape_or_is_child_shape(self, s: Shape) -> bool:
        return self == s or self.left.is_equal_to_shape_or_is_child_shape(s) or self.right.is_equal_to_shape_or_is_child_shape(s)

    def local_intersect(self, ray: Ray) -> List[tuple[float, Shape, float, float]]:
        transformed_ray = ray.get_transformed_ray(self.ray_transform)
        xs = self.left.local_intersect(transformed_ray) + self.right.local_intersect(transformed_ray)
        xs = sorted(xs, key=lambda intersection: intersection[0])
        return self.filter_intersections(xs)
    
    def is_out_of_bounds(self, ray: Ray) -> bool:
        bounds = self.bounds()
        xtmin, xtmax = Group.check_axis(bounds.min_point.x, bounds.max_point.x, ray.origin.x, ray.direction.x)
        ytmin, ytmax = Group.check_axis(bounds.min_point.y, bounds.max_point.y, ray.origin.y, ray.direction.y)
        ztmin, ztmax = Group.check_axis(bounds.min_point.z, bounds.max_point.z, ray.origin.z, ray.direction.z)
        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)
        return tmin > tmax
    
    def memoize_bounds(self) -> None:
        self.memoized_bounds = Bounds.find_bounds_of_group_of_bounds([self.left.bounds(), self.right.bounds()])
    
    def normal_at(self, point: Point, u: float, v: float) -> Vector:
        raise NotImplementedError('This method should not be called for groups')
    
    def bounds(self) -> Bounds:
        return self.memoized_bounds

    @staticmethod
    def is_intersection_allowed(operation: CSGOperation, is_left_hit: bool, is_in_left: bool, is_in_right: bool) -> bool:
        if operation == CSGOperation.UNION:
            return (is_left_hit and not is_in_right) or (not is_left_hit and not is_in_left)
        elif operation == CSGOperation.INTERSECTION:
            return (is_left_hit and is_in_right) or (not is_left_hit and is_in_left)
        elif operation == CSGOperation.DIFFERENCE:
            return (is_left_hit and not is_in_right) or (not is_left_hit and is_in_left)
        return False