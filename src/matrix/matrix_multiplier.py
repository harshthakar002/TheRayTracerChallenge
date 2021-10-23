from matrix.matrix import Matrix

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
