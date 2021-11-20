from patterns.pattern import Pattern
from patterns.two_patterned_pattern import TwoPatternedPattern
from features.point import Point
from features.color import Color
from math import floor
from figures.figure import Figure

class StripePattern(TwoPatternedPattern):
    
    def color_at_object_point(self, object: Figure, point: Point) -> Color:
        object_point = object.ray_origin_transform.multiply_matrix_and_tuple(point)
        pattern_point = self.transform.multiply_matrix_and_tuple(object_point)
        if floor(pattern_point.x) % 2:
            return self.pattern2.color_at_object_point(object, pattern_point)
        return self.pattern1.color_at_object_point(object, pattern_point)