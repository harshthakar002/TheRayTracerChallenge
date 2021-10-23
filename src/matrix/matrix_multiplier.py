from matrix.matrix import Matrix
from features.tuple import Tuple

class MatrixMultiplier():

    @staticmethod
    def multiply_matrices(m1: Matrix, m2: Matrix) -> Matrix:
        result = []
        for i in range(m1.row_count):
            result.append([])
            for k in range(m2.column_count):
                c = 0
                for j in range(m1.column_count):
                    c += m1.get(i, j) * m2.get(j, k)
                result[i].append(c)
        return Matrix.initialize_from_values(result)
    
    @staticmethod
    def multiply_matrix_and_tuple(m: Matrix, t: Tuple) -> Tuple:
        return Tuple(m.get(0, 0) * t.x + m.get(0, 1) * t.y + m.get(0, 2) * t.z + m.get(0, 3) * t.w,
        m.get(1, 0) * t.x + m.get(1, 1) * t.y + m.get(1, 2) * t.z + m.get(1, 3) * t.w,
        m.get(2, 0) * t.x + m.get(2, 1) * t.y + m.get(2, 2) * t.z + m.get(2, 3) * t.w,
        m.get(3, 0) * t.x + m.get(3, 1) * t.y + m.get(3, 2) * t.z + m.get(3, 3) * t.w)
