from patterns.pattern import Pattern
from patterns.two_patterned_pattern import TwoPatternedPattern
from features.color import Color
from features.vector import Vector
from features.point import Point
from math import floor

class GradientPattern(TwoPatternedPattern):
    
    def color_at(self, point: Point) -> Color:
        if floor(point.x) % 2:
            a = self.pattern2.color_at(point)
            b = self.pattern1.color_at(point)
        else:
            a = self.pattern1.color_at(point)
            b = self.pattern2.color_at(point)
        color_delta = b - a
        distance = Vector(color_delta.x, color_delta.y, color_delta.z)
        fraction = point.x - floor(point.x)
        color_movement = distance * fraction 
        return a + Color(color_movement.x, color_movement.y, color_movement.z)
