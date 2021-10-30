from features.color import Color
from features.point import Point

class Light():
    def __init__(self, intensity: Color, position: Point) -> None:
        self.intensity = intensity
        self.position = position