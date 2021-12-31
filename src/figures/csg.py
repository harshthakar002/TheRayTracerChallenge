from enum import Enum, unique
from figures.shape import Shape

@unique
class CSGOperation(Enum):
    UNION = 'UNION'
    INTERSECTION = 'INTERSECTION'
    DIFFERENCE = 'DIFFERENCE'


class CSG(Shape):

    def __init__(self, operation: CSGOperation, left: Shape, right: Shape):
        self.operation = operation
        self.left = left
        left.parent = self
        self.right = right
        right.parent = self

    @staticmethod
    def is_intersection_allowed(operation: CSGOperation, is_left_hit: bool, is_in_left: bool, is_in_right: bool) -> bool:
        if operation == CSGOperation.UNION:
            return (is_left_hit and not is_in_right) or (not is_left_hit and not is_in_left)
        elif operation == CSGOperation.INTERSECTION:
            return (is_left_hit and is_in_right) or (not is_left_hit and is_in_left)
        return False