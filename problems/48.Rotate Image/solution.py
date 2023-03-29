from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transponse(matrix)
        self.reflect(matrix)

    def transponse(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        for i in range(size):
            for j in range(i + 1, size):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        for i in range(size):
            for j in range(size // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
