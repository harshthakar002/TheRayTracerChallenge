from typing import Tuple as Group
from matrix.matrix import Matrix
from transformations.transformer import Transformer

class RayTransformer():

    @staticmethod
    def translation(x: float, y: float, z: float) -> Group[Matrix, Matrix]:
        m = Transformer.translation(x, y, z)
        return m, Matrix.generate_identity_matrix(4)
    
    @staticmethod
    def scaling(x: float, y: float, z: float) -> Group[Matrix, Matrix]:
        m = Transformer.scaling(x, y, z)
        return m, m