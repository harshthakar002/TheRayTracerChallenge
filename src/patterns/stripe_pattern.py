from patterns.pattern import Pattern
from patterns.two_patterned_pattern import TwoPatternedPattern
from features.point import Point
from features.color import Color
from math import floor

class StripePattern(TwoPatternedPattern):
    
    def color_at(self, point: Point) -> Color:
        if floor(point.x) % 2:
            return self.pattern2.color_at(point)
        return self.pattern1.color_at(point)