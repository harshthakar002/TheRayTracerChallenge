from matrix.matrix import Matrix
from matrix.matrix_inverter import MatrixInverter
from features.equality import is_approximately_equal

def test_determinant_for_2_x_2_matrix():
    m = Matrix.initialize_from_values([[1, 5], [-3, 2]])
    assert is_approximately_equal(MatrixInverter.calculate_determinant_for_2_x_2_matrix(m), 17)