from features.equality import isApproximatelyEqual


class tuple:

    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        self.x, self.y, self.z, self.w = x, y, z, w
    
    def __add__(self, o: tuple) -> tuple:
        return tuple(self.x + o.x, self.y + o.y, self.z + o.z, self.w + o.w)

    def __sub__(self, o: tuple) -> tuple:
        return tuple(self.x - o.x, self.y - o.y, self.z - o.z, self.w - o.w)
    
    def __mul__(self, o: float) -> tuple:
        return tuple(self.x * o, self.y * o, self.z * o, self.w * o)

    def __truediv__(self, o: float) -> tuple:
        return tuple(self.x / o, self.y / o, self.z / o, self.w / o)

    def __eq__(self, o: tuple) -> bool:
        return isApproximatelyEqual(self.x, o.x) and isApproximatelyEqual(self.y, o.y) and isApproximatelyEqual(self.z, o.z) and isApproximatelyEqual(self.w, o.w)

    def __ne__(self, o: tuple) -> bool:
        return not (self == o)

    def isPoint(self) -> bool:
        return isApproximatelyEqual(self.w, 1.0)

    def isVector(self) -> bool:
        return isApproximatelyEqual(self.w, 0.0)
    
    def negate(self) -> tuple:
        return tuple(-self.x, -self.y, -self.z, -self.w)