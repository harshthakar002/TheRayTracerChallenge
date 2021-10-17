from features.tuple import tuple

class point(tuple):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z, 1.0)