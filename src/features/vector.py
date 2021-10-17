from features.tuple import tuple

class vector(tuple):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z, 0.0)

ZERO_VECTOR = vector(0, 0, 0)