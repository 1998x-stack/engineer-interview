from __future__ import annotations
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_col_zero = any(matrix[r][0] == 0 for r in range(m))
        first_row_zero = any(matrix[0][c] == 0 for c in range(n))
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if first_row_zero:
            for c in range(n): matrix[0][c] = 0
        if first_col_zero:
            for r in range(m): matrix[r][0] = 0
