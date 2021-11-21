from features.color import Color
from features.point import Point
from patterns.pattern import Pattern

class TestPattern(Pattern):

    def color_at(self, point: Point) -> Color:
        return Color(point.x, point.y, point.z)