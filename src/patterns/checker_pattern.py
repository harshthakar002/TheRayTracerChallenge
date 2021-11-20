from patterns.pattern import Pattern
from features.point import Point
from features.color import Color
from math import floor

class CheckerPattern(Pattern):

    def __init__(self, color1: Color, color2: Color) -> None:
        self.color1 = color1
        self.color2 = color2
        super().__init__()
    
    def color_at(self, point: Point) -> Color:
        if (floor(point.x) + floor(point.y) + floor(point.z)) % 2:
            return self.color2
        return self.color1