from patterns.pattern import Pattern
from features.color import Color
from features.point import Point

class SolidPattern(Pattern):

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()
    
    def color_at(self, point: Point) -> Color:
        return self.color