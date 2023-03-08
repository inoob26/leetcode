from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # more elegant
        return [
            [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))
        ]

        # ny solution
        # rows, cols = len(matrix), len(matrix[0])
        # result = []
        # for col in range(cols):
        #     tmp = []
        #     for row in range(rows):
        #         tmp.append(matrix[row][col])
        #     result.append(tmp)
        # return result
