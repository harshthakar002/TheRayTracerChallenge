from __future__ import annotations
from features.color import Color
from features.equality import is_approximately_equal

class Material():

    def __init__(self, color: Color=Color(1, 1, 1), ambient:float=0.1, diffuse:float=0.9, specular:float=0.9, shininess:float=200.0) -> None:
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
    
    def __eq__(self, o: Material) -> bool:
        return (self.color == o.color and
        is_approximately_equal(self.ambient, o.ambient) and
        is_approximately_equal(self.diffuse, o.diffuse) and
        is_approximately_equal(self.specular, o.specular) and
        is_approximately_equal(self.shininess, o.shininess))
