from figures.figure import Figure
from patterns.two_patterned_pattern import TwoPatternedPattern
from patterns.pattern import Pattern
from features.color import Color
from features.point import Point

class BlendedPattern(TwoPatternedPattern):

    def color_at_object_point(self, object: Figure, point: Point) -> Color:
        object_point = object.ray_origin_transform.multiply_matrix_and_tuple(point)
        pattern_point = self.transform.multiply_matrix_and_tuple(object_point)
        color1 = self.pattern1.color_at_object_point(object, pattern_point)
        color2 = self.pattern2.color_at_object_point(object, pattern_point)
        return Color((color1.red + color2.red) / 2, (color1.green + color2.green) / 2, (color1.blue + color2.blue) / 2)