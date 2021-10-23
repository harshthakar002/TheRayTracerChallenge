from __future__ import annotations
from typing import List
from features.equality import is_approximately_equal

class Matrix():
    def __init__(self, row_count: int, column_count: int) -> None:
        self.row_count = row_count
        self.column_count = column_count
        self.data = []
        for i in range(row_count):
            self.data.append([])
            for j in range(column_count):
                self.data[i].append(0.0)
    
    @staticmethod
    def initialize_from_values(values: List[List[float]]) -> Matrix:
        mat = Matrix(len(values), len(values[0]))
        mat.data = values
        return mat

    @staticmethod
    def generate_identity_matrix(row_and_column_count: int) -> Matrix:
        mat = Matrix(row_and_column_count, row_and_column_count)
        for i in range(row_and_column_count):
            mat.set(i, i, 1)
        return mat
    
    def get(self, i: int, j: int) -> float:
        return self.data[i][j]
    
    def set(self, i: int, j: int, value: float) -> None:
        self.data[i][j] = value

    def __eq__(self, mat: Matrix) -> bool:
        if self.row_count != mat.row_count or self.column_count != mat.column_count:
            return False
        for i in range(self.row_count):
            for j in range(self.column_count):
                if not is_approximately_equal(self.get(i, j), mat.get(i, j)):
                    return False
        return True
    
    def __ne__(self, mat: Matrix) -> bool:
        return not self == mat
    
    def transposed_matrix(self) -> Matrix:
        transposed_matrix = Matrix(self.row_count, self.column_count)
        for i in range(self.row_count):
            for j in range(self.column_count):
                transposed_matrix.set(j, i, self.get(i, j))
        return transposed_matrix