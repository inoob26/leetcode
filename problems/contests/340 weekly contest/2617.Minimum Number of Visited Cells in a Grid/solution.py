from typing import List

"""
passed all tests
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        bestRow = [[] for _ in range(m)] # will store (minScore, maxReachableColumn) for each row
        bestCol = [[] for _ in range(n)] # will store (minScore, maxReachableRow) for each column
        
        finf = float('inf')
        heappush(bestRow[0], (1, 0))
        for i in range(m):
            for j in range(n):
                minScore = finf

                # removing scores that are not reaching this cell
                while bestRow[i] and bestRow[i][0][1] < j:
                    heappop(bestRow[i])
                if bestRow[i]:
                    minScore = min(minScore, bestRow[i][0][0])

                # removing scores that are not reaching this cell
                while bestCol[j] and bestCol[j][0][1] < i:
                    heappop(bestCol[j])
                if bestCol[j]:
                    minScore = min(minScore, bestCol[j][0][0])

                if (i,j) == (m-1, n-1) and minScore != finf:
                    return minScore
                if minScore != finf:
                    heappush(bestRow[i], (minScore+1, j+grid[i][j]))
                    heappush(bestCol[j], (minScore+1, i+grid[i][j]))
        
        return -1
"""


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        furthest_in_row = [0 for _ in range(cols)]
        furthest_in_col = [0 for _ in range(rows)]

        #         r  c  count
        queue = [(0, 0, 1)]

        while queue:
            row, col, count = queue.pop(0)

            if row == rows - 1 and col == cols - 1:
                return count

            start_row = max(furthest_in_row[col], row) + 1
            end_row = min(grid[row][col] + row, rows - 1)
            for k_row in range(start_row, end_row + 1):
                queue.append((k_row, col, count + 1))

            start_col = max(furthest_in_col[row], col) + 1
            end_col = min(grid[row][col] + col, cols - 1)
            for k_col in range(start_col, end_col + 1):
                queue.append((row, k_col, count + 1))

            furthest_in_row[col] = max(furthest_in_row[col], end_row)
            furthest_in_col[row] = max(furthest_in_col[row], end_col)

        return -1
