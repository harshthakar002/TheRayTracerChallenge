from matrix.matrix import Matrix
from math import tan

class Camera():

    def __init__(self, hsize: float, vsize: float, field_of_view: float, transform: Matrix = Matrix.generate_identity_matrix(4)) -> None:
        self.hsize = hsize
        self.vside = vsize
        self.field_of_view = field_of_view
        self.transform = transform
        half_view = tan(self.field_of_view / 2)
        aspect = self.hsize / self.vside

        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view
        
        self.pixel_size = (self.half_width * 2) / self.hsize
        