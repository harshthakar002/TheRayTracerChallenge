from uuid import uuid4
from figures.ray import Ray
from typing import List

class Figure():

    def __init__(self):
        self.id = uuid4().int
    
    def ray_intersection_distance(self, ray: Ray) -> List[float]:
        raise NotImplementedError('Abstract method')