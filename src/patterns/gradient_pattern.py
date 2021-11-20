from patterns.pattern import Pattern
from patterns.two_patterned_pattern import TwoPatternedPattern
from features.color import Color
from features.vector import Vector
from features.point import Point
from math import floor
from figures.figure import Figure

class GradientPattern(TwoPatternedPattern):
    
    def color_at_object_point(self, object: Figure, point: Point) -> Color:
        object_point = object.ray_origin_transform.multiply_matrix_and_tuple(point)
        pattern_point = self.transform.multiply_matrix_and_tuple(object_point)
        if floor(pattern_point.x) % 2:
            a = self.pattern2.color_at_object_point(object, pattern_point)
            b = self.pattern1.color_at_object_point(object, pattern_point)
        else:
            a = self.pattern1.color_at_object_point(object, pattern_point)
            b = self.pattern2.color_at_object_point(object, pattern_point)
        color_delta = b - a
        distance = Vector(color_delta.x, color_delta.y, color_delta.z)
        fraction = pattern_point.x - floor(pattern_point.x)
        color_movement = distance * fraction 
        return a + Color(color_movement.x, color_movement.y, color_movement.z)
