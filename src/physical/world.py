from typing import List
from physical.light import Light
from figures.shape import Shape

class World():

    def __init__(self) -> None:
        self.light: Light = None
        self.objects: List[Shape] = [] 
