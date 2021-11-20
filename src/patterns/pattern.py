from features.color import Color
from features.point import Point

class Pattern():

    def __init__(self) -> None:
        raise NotImplementedError('Cannot instantiate Pattern')

    def color_at(self, point: Point) -> Color:
        raise NotImplementedError('Not implemented for base class')