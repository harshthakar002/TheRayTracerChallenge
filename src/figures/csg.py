from enum import Enum, unique
from typing import List
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

    @staticmethod
    def is_intersection_allowed(operation: CSGOperation, is_left_hit: bool, is_in_left: bool, is_in_right: bool) -> bool:
        if operation == CSGOperation.UNION:
            return (is_left_hit and not is_in_right) or (not is_left_hit and not is_in_left)
        elif operation == CSGOperation.INTERSECTION:
            return (is_left_hit and is_in_right) or (not is_left_hit and is_in_left)
        elif operation == CSGOperation.DIFFERENCE:
            return (is_left_hit and not is_in_right) or (not is_left_hit and is_in_left)
        return False