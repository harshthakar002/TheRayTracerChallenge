from __future__ import annotations
from features.tuple import tuple
from features.equality import isApproximatelyEqual

class color(tuple):

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
    
    def __add__(self, o: color) -> color:
        return color(self.red + o.red, self.green + o.green, self.blue + o.blue)

    def __sub__(self, o: color) -> color:
        return color(self.red - o.red, self.green - o.green, self.blue - o.blue)
    
    def __mul__(self, o: float) -> color:
        return color(self.red * o, self.green * o, self.blue * o)

    def __truediv__(self, o: float) -> color:
        return color(self.red / o, self.green / o, self.blue / o)
