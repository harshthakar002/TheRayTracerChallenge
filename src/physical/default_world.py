from physical.light import Light
from physical.world import World
from physical.point_light import PointLight
from figures.sphere import Sphere
from features.color import Color
from features.point import Point
from transformations.figure_transformer import FigureTransformer

class DefaultWorld(World):

    def __init__(self) -> None:
        super().__init__()
        light = PointLight(Color(1, 1, 1), Point(-10, 10, -10))
        s1 = Sphere()
        s1.material.color = Color(0.8, 1.0, 0.6)
        s1.material.diffuse = 0.7
        s1.material.specular = 0.2
        s2 = Sphere()
        s2.scaling(0.5, 0.5, 0.5)
        self.light = light
        self.objects.append(s1)
        self.objects.append(s2)
