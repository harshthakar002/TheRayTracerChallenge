from __future__ import annotations
from features.color import Color
from features.point import Point

class Light():
    def __init__(self, intensity: Color, position: Point) -> None:
        self.intensity = intensity
        self.position = position
    
    def __eq__(self, o: Light) -> bool:
        return self.position == o.position and self.intensity == o.intensity