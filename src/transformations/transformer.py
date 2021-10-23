from matrix.matrix import Matrix

class Transformer():

    @staticmethod
    def translation(x: int, y: int, z: int) -> Matrix:
        translation_matrix = Matrix.generate_identity_matrix(4)
        translation_matrix.set(0, 3, x)
        translation_matrix.set(1, 3, y)
        translation_matrix.set(2, 3, z)
        return translation_matrix