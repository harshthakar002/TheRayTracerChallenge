from matrix.matrix import Matrix
from matrix.matrix_inverter import MatrixInverter
from features.equality import is_approximately_equal

def test_determinant_for_2_x_2_matrix():
    m = Matrix.initialize_from_values([[1, 5], [-3, 2]])
    assert is_approximately_equal(MatrixInverter.calculate_determinant_for_2_x_2_matrix(m), 17)

def test_sub_matrix_of_3_x_3_matrix():
    m = Matrix.initialize_from_values([[1, 5, 0], [-3, 2, 7], [0, 6, -3]])
    sub_matrix = MatrixInverter.create_sub_matrix(m, 0, 2)
    excepted_result = m.initialize_from_values([[-3, 2], [0, 6]])
    assert sub_matrix.row_count == 2
    assert sub_matrix.column_count == 2
    assert sub_matrix == excepted_result

def test_sub_matrix_of_4_x_4_matrix():
    m = Matrix.initialize_from_values([[-6, 1, 1, 6], [-8, 5, 8, 6], [-1, 0, 8, 2], [-7, 1, -1, 1]])
    expected_result = Matrix.initialize_from_values([[-6, 1, 6], [-8, 8, 6], [-7, -1, 1]])
    sub_matrix = MatrixInverter.create_sub_matrix(m, 2, 1)
    assert sub_matrix.row_count == 3
    assert sub_matrix.column_count == 3
    assert sub_matrix == expected_result

def test_minor_of_3_x_3_matrix():
    m = Matrix.initialize_from_values([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
    assert is_approximately_equal(MatrixInverter.calculate_minor_for_3_x_3_matrix(m, 1, 0), 25)

def test_cofactor_of_3_x_3_matrix():
    m = Matrix.initialize_from_values([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
    assert is_approximately_equal(MatrixInverter.calculate_minor_for_3_x_3_matrix(m, 0, 0), -12)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 0), -12)
    assert is_approximately_equal(MatrixInverter.calculate_minor_for_3_x_3_matrix(m, 1, 0), 25)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 1, 0), -25)

def test_determinant_of_3_x_3_matrix():
    m = Matrix.initialize_from_values([[1, 2, 6], [-5, 8, -4], [2, 6, 4]])
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 0), 56)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 1), 12)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 2), -46)
    assert is_approximately_equal(MatrixInverter.calculate_determinant(m), -196)

def test_determinant_of_4_x_4_matrix():
    m = Matrix.initialize_from_values([[-2, -8, 3, 5], [-3, 1, 7, 3], [1, 2, -9, 6], [-6, 7, 7, -9]])
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 0), 690)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 1), 447)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 2), 210)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 3), 51)
    assert is_approximately_equal(MatrixInverter.calculate_determinant(m), -4071)

def test_is_matrix_is_not_invertible():
    m = Matrix.initialize_from_values([[-4, 2, -2, -3], [9, 6, 2, 6], [0, -5, 1, -5], [0, 0, 0, 0]])
    assert MatrixInverter.invert(m) == None
    assert MatrixInverter.calculate_determinant(m) == 0

def test_invert_of_matrix():
    m = Matrix.initialize_from_values([[-5, 2, 6, -8], [1, -5, 1, 8], [7, 7, -6, -7], [1, -3, 7, 4]])
    inverse_m = MatrixInverter.invert(m)
    assert is_approximately_equal(MatrixInverter.calculate_determinant(m), 532)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 2, 3), -160)
    assert is_approximately_equal(inverse_m.get(3, 2), -160 / 532)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 3, 2), 105)
    assert is_approximately_equal(inverse_m.get(2, 3), 105 / 532)
    expected_result = Matrix.initialize_from_values([[0.21805, 0.45113, 0.24060, -0.04511], [-0.80827, -1.45677, -0.44361, 0.52068],
    [-0.07895, -0.22368, -0.05263, 0.19737], [-0.52256, -0.81391, -0.30075, 0.30639]])
    assert inverse_m == expected_result

def test_invert_of_matrix_2():
    m = Matrix.initialize_from_values([[8, -5, 9, 2], [7, 5, 6, 1], [-6, 0, 9, 6], [-3, 0, -9, -4]])
    inverse_m = MatrixInverter.invert(m)
    expected_result = Matrix.initialize_from_values([
    [-0.15385, -0.15385, -0.28205, -0.53846],
    [-0.07692, 0.12308, 0.02564, 0.03077],
    [0.35897, 0.35897, 0.43590, 0.92308],
    [-0.69231, -0.69231, -0.76923, -1.92308]])
    assert inverse_m == expected_result

def test_invert_of_matrix_3():
    m = Matrix.initialize_from_values([[9, 3, 0, 9], [-5, -2, -6, -3], [-4, 9, 6, 4], [-7, 6, 6, 2]])
    inverse_m = MatrixInverter.invert(m)
    expected_result = Matrix.initialize_from_values([
    [-0.04074, -0.07778, 0.14444, -0.22222],
    [-0.07778, 0.03333, 0.36667, -0.33333],
    [-0.02901, -0.14630, -0.10926, 0.12963],
    [0.17778, 0.06667, -0.26667, 0.33333]])
    assert inverse_m == expected_result

def test_multiply_product_by_inverse():
    a = Matrix.initialize_from_values([[3, -9, 7, 3], [3, -8, 2, -9], [-4, 4, 4, 1], [-6, 5, -1, 1]])
    b = Matrix.initialize_from_values([[8, 2, 2, 2], [3, -1, 7, 0], [7, 0, 5, 4], [6, -2, 0, 5]])
    c = a.multiply_matrices(b)
    b_inverse = MatrixInverter.invert(b)
    assert c.multiply_matrices(b_inverse) == a

def test_inverting_identity_matrix():
    identity_matrix = Matrix.generate_identity_matrix(4)
    identity_matrix_inverse = MatrixInverter.invert(identity_matrix)
    assert identity_matrix == identity_matrix_inverse

def test_multiply_matrix_by_inverse():
    m = Matrix.initialize_from_values([[9, 3, 0, 9], [-5, -2, -6, -3], [-4, 9, 6, 4], [-7, 6, 6, 2]])
    inverse_m = MatrixInverter.invert(m)
    result = m.multiply_matrices(inverse_m)
    assert result == Matrix.generate_identity_matrix(4)