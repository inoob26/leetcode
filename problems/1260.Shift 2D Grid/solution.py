from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        while k > 0:
            previous = grid[-1][-1]
            for row in range(rows):
                for col in range(cols):
                    temp = grid[row][col]
                    grid[row][col] = previous
                    previous = temp
            k -= 1

        return grid

        # my solution
        # rows, cols = len(grid), len(grid[0])
        # while k > 0:
        #     dp = [[None] * cols for _ in range(rows)]
        #     # first shift
        #     dp[0][0] = grid[rows - 1][cols - 1]

        #     for row in range(1, rows):
        #         dp[row][0] = grid[row - 1][cols - 1]
        #     # others shift
        #     for row in range(rows):
        #         for col in range(1, cols):
        #             dp[row][col] = grid[row][col - 1]

        #     grid = dp
        #     k -= 1
        # return grid
