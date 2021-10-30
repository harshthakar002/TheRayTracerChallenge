from typing import List
from physical.light import Light
from figures.figure import Figure

class World():

    def __init__(self) -> None:
        self.light: Light = None
        self.objects: List[Figure] = [] 
