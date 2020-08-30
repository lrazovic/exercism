from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        matrix: List[str] = matrix_string.split("\n")
        self.rows: List[List[int]] = [list(map(int, x.split())) for x in matrix]
        self.cols: List[List[int]] = [list(l) for l in zip(*self.rows)]

    def row(self, index: int) -> List[int]:
        return self.rows[index - 1]

    def column(self, index: int) -> List[int]:
        return self.cols[index - 1]
