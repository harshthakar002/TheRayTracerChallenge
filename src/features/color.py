from __future__ import annotations
from features.tuple import Tuple

class Color(Tuple):

    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z, 2.0)
    
    @property
    def red(self) -> float:
        return self.x
    
    @red.setter
    def red(self, value: float) -> None:
        self.x = value
    
    @property
    def green(self) -> float:
        return self.y
    
    @green.setter
    def green(self, value: float) -> None:
        self.y = value
    
    @property
    def blue(self) -> float:
        return self.z
    
    @blue.setter
    def blue(self, value: float) -> None:
        self.z = value
    
    def __add__(self, o: Color) -> Color:
        return Color(self.red + o.red, self.green + o.green, self.blue + o.blue)

    def __sub__(self, o: Color) -> Color:
        return Color(self.red - o.red, self.green - o.green, self.blue - o.blue)
    
    def __mul__(self, o: float) -> Color:
        return Color(self.red * o, self.green * o, self.blue * o)

    def __truediv__(self, o: float) -> Color:
        return Color(self.red / o, self.green / o, self.blue / o)

    def multiply(self, c: Color) -> Color:
        return Color(self.red * c.red, self.green * c.green, self.blue * c.blue)

BLACK_COLOR = Color(0, 0, 0)
WHITE_COLOR = Color(1, 1, 1)
