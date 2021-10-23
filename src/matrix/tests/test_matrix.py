from matrix.matrix import matrix
from features.equality import is_approximately_equal

def test_matrix_creation():
    mat = matrix(4, 4)
    assert mat.row_count == 4
    assert mat.column_count == 4
    assert mat.data == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def test_matrix_construction():
    mat = matrix(4, 4)
    assert mat.row_count == 4
    assert mat.column_count == 4
    mat.initialize([[1, 2, 3, 4], [5.5, 6.5, 7.5, 8.5], [9, 10, 11, 12],[13.5, 14.5, 15.5, 16.5]])
    is_approximately_equal(mat.get(0, 0), 1)
    is_approximately_equal(mat.get(0, 1), 2)
    is_approximately_equal(mat.get(0, 2), 3)
    is_approximately_equal(mat.get(0, 3), 4)
    is_approximately_equal(mat.get(1, 0), 5.5)
    is_approximately_equal(mat.get(1, 1), 6.5)
    is_approximately_equal(mat.get(1, 2), 7.5)
    is_approximately_equal(mat.get(1, 3), 8.5)
    is_approximately_equal(mat.get(2, 0), 9)
    is_approximately_equal(mat.get(2, 1), 10)
    is_approximately_equal(mat.get(2, 2), 11)
    is_approximately_equal(mat.get(2, 3), 12)
    is_approximately_equal(mat.get(3, 0), 13.5)
    is_approximately_equal(mat.get(3, 1), 14.5)
    is_approximately_equal(mat.get(3, 2), 15.5)
    is_approximately_equal(mat.get(3, 3), 16.5)