from typing import List


class matrix():
    def __init__(self, row_count: int, column_count: int) -> None:
        self.row_count = row_count
        self.column_count = column_count
        self.data = []
        for i in range(row_count):
            self.data.append([])
            for j in range(column_count):
                self.data[i].append(0.0)
    
    def initialize(self, data: List[List[float]]) -> None:
        self.data = data
    
    def get(self, i: int, j: int) -> float:
        return self.data[i][j]
    
    def set(self, i: int, j: int, value: float) -> None:
        self.data[i][j] = value