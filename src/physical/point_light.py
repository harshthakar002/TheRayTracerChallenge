from features.color import Color
from features.point import Point
from physical.light import Light

class PointLight(Light):

    def __init__(self, intensity: Color, position: Point) -> None:
        super().__init__(intensity, position)