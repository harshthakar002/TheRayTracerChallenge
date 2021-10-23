from __future__ import annotations
from features.equality import is_approximately_equal


class Tuple:

    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        self.x, self.y, self.z, self.w = x, y, z, w
    
    def __add__(self, o: Tuple) -> Tuple:
        return Tuple(self.x + o.x, self.y + o.y, self.z + o.z, self.w + o.w)

    def __sub__(self, o: Tuple) -> Tuple:
        return Tuple(self.x - o.x, self.y - o.y, self.z - o.z, self.w - o.w)
    
    def __mul__(self, o: float) -> Tuple:
        return Tuple(self.x * o, self.y * o, self.z * o, self.w * o)

    def __truediv__(self, o: float) -> Tuple:
        return Tuple(self.x / o, self.y / o, self.z / o, self.w / o)

    def __eq__(self, o: Tuple) -> bool:
        return is_approximately_equal(self.x, o.x) and is_approximately_equal(self.y, o.y) and is_approximately_equal(self.z, o.z) and is_approximately_equal(self.w, o.w)

    def __ne__(self, o: Tuple) -> bool:
        return not (self == o)

    def is_point(self) -> bool:
        return is_approximately_equal(self.w, 1.0)

    def is_vector(self) -> bool:
        return is_approximately_equal(self.w, 0.0)
    
    def negate(self) -> Tuple:
        return Tuple(-self.x, -self.y, -self.z, -self.w)