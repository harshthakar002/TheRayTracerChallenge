from patterns.pattern import Pattern
from features.color import Color
from features.vector import Vector
from features.point import Point
from math import floor

class GradientPattern(Pattern):

    def __init__(self, color1: Color, color2: Color) -> None:
        self.color1 = color1
        self.color2 = color2
        super().__init__()
    
    def color_at(self, point: Point) -> Color:
        if floor(point.x) % 2:
            a = self.color2
            b = self.color1
        else:
            a = self.color1
            b = self.color2
        color_delta = b - a
        distance = Vector(color_delta.x, color_delta.y, color_delta.z)
        fraction = point.x - floor(point.x)
        color_movement = distance * fraction 
        return a + Color(color_movement.x, color_movement.y, color_movement.z)
