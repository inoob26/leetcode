from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        expected = r * c
        current = len(mat) * len(mat[0])
        if expected != current:
            return mat

        result = [[0] * c for i in range(r)]
        rows, cols = 0, 0
        for row_i in range(len(mat)):
            for col_i in range(len(mat[0])):
                result[rows][cols] = mat[row_i][col_i]
                cols += 1
                if cols == c:
                    cols = 0
                    rows += 1

        return result
