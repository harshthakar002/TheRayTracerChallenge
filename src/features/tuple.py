from features.equality import isApproximatelyEqual

class tuple:

    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        self.x, self.y, self.z, self.w = x, y, z, w

    def isPoint(self) -> bool:
        return isApproximatelyEqual(self.w, 1.0)

    def isVector(self) -> bool:
        return isApproximatelyEqual(self.w, 0.0)
