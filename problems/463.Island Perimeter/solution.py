from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # more readable
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    result += 4

                    # have up neighbor
                    if row > 0 and grid[row - 1][col] == 1:
                        result -= 2
                    if col > 0 and grid[row][col - 1] == 1:
                        result -= 2

        return result
        # my solution
        # rows = len(grid)
        # cols = len(grid[0])
        # result = 0
        # for row in range(rows):
        #     for col in range(cols):
        #         cur = grid[row][col]
        #         if cur == 0:
        #             continue
        #         # left
        #         if col != 0 and grid[row][col - 1] == 0:
        #             result += 1
        #         elif col == 0:
        #             result += 1
        #         # right
        #         if col != cols - 1 and grid[row][col + 1] == 0:
        #             result += 1
        #         elif col == cols - 1:
        #             result += 1
        #         # up
        #         if row != 0 and grid[row - 1][col] == 0:
        #             result += 1
        #         elif row == 0:
        #             result += 1

        #         # down
        #         if row != rows - 1 and grid[row + 1][col] == 0:
        #             result += 1
        #         elif row == rows - 1:
        #             result += 1
        # return result
