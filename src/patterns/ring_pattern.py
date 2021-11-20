from patterns.pattern import Pattern
from features.color import Color
from features.point import Point
from math import floor, sqrt

class RingPattern(Pattern):

    def __init__(self, color1: Color, color2: Color) -> None:
        self.color1 = color1
        self.color2 = color2
        super().__init__()

    def color_at(self, point: Point) -> Color:
        if floor(sqrt((point.x * point.x) + (point.z * point.z))) % 2:
            return self.color2
        return self.color1