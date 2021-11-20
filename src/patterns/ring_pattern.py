from patterns.pattern import Pattern
from patterns.two_patterned_pattern import TwoPatternedPattern
from features.color import Color
from features.point import Point
from math import floor, sqrt

class RingPattern(TwoPatternedPattern):

    def color_at(self, point: Point) -> Color:
        if floor(sqrt((point.x * point.x) + (point.z * point.z))) % 2:
            return self.pattern2.color_at(point)
        return self.pattern1.color_at(point)