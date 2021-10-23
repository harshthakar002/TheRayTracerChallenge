from matrix.matrix import Matrix
from matrix.matrix_multiplier import MatrixMultiplier
from features.tuple import Tuple

def test_matrix_multiplication():
    a = Matrix.initialize_from_values([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    b = Matrix.initialize_from_values([[-2, 1, 2, 3], [3, 2, 1, -1], [4, 3, 6, 5], [1, 2, 7, 8]])
    c = Matrix.initialize_from_values([[20, 22, 50, 48], [44, 54, 114, 108], [40, 58, 110, 102], [16, 26, 46, 42]])
    assert MatrixMultiplier.multiply_matrices(a, b) == c

def test_matrix_multiplication_with_tuple():
    m = Matrix.initialize_from_values([[1, 2, 3, 4], [2, 4, 4, 2], [8, 6, 4, 1], [0, 0, 0, 1]])
    t = Tuple(1, 2, 3, 1)
    expected_result = Tuple(18, 24, 33, 1)
    assert MatrixMultiplier.multiply_matrix_and_tuple(m, t) == expected_result