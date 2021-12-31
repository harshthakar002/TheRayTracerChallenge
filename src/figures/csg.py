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