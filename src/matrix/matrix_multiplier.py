from matrix.matrix import matrix

class MatrixMultiplier():

    @staticmethod
    def multiply_matrices(m1: matrix, m2: matrix) -> matrix:
        result = []
        for i in range(m1.row_count):
            result.append([])
            for k in range(m2.column_count):
                c = 0
                for j in range(m1.column_count):
                    c += m1.get(i, j) * m2.get(j, k)
                result[i].append(c)
        return matrix.initialize_from_values(result)
