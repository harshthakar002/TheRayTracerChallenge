from __future__ import annotations
from features.tuple import Tuple

class Point(Tuple):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z, 1.0)
    
    @staticmethod
    def fromTuple(t: Tuple) -> Point:
        if not t.is_point():
            raise TypeError('Can\'t convert non-point tuple to point')
        return Point(t.x, t.y, t.z)