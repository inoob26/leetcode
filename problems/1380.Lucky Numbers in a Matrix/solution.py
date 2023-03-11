from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) < 2:
            return matrix

        rows = len(matrix)
        min_map = {}
        for row_indx, row in enumerate(matrix):
            min_row = min(row)
            col_indx = row.index(min_row)
            min_map[min_row] = (row_indx, col_indx)

        for row_val, indexes in min_map.items():
            max_val = max([matrix[row][indexes[1]] for row in range(rows)])
            if max_val == row_val:
                return [row_val]
