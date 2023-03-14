from typing import List, Dict
from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # v2
        N = 9

        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for row in range(N):
            for col in range(N):
                if board[row][col] == ".":
                    continue

                position = int(board[row][col]) - 1

                if rows[row][position] == 1:
                    return False
                rows[row][position] = 1

                if cols[col][position] == 1:
                    return False
                cols[col][position] = 1

                indx = (row // 3) * 3 + col // 3
                if boxes[indx][position] == 1:
                    return False
                boxes[indx][position] = 1
        return True
        # my solution
        # rows, cols = 9, 9

        # def has_repeted_values(values_map: Dict[str, int]) -> bool:
        #     for key, val in values_map.items():
        #         if key != "." and val > 1:
        #             return True
        #     return False

        # def check_rows() -> bool:
        #     for r in range(rows):
        #         row_map = Counter(board[r])
        #         if has_repeted_values(values_map=row_map):
        #             return False
        #     return True

        # def check_cols() -> bool:
        #     for c in range(cols):
        #         col_map = Counter(board[r][c] for r in range(rows))
        #         if has_repeted_values(values_map=col_map):
        #             return False
        #     return True

        # if not check_rows() or not check_cols():
        #     return False

        # row = 3
        # col = 3
        # indx = 0
        # step = 3
        # row_indx = 0
        # while row <= rows and col <= cols:
        #     # check rectangle
        #     tmp_lst = []
        #     for r in range(row_indx, row):
        #         for c in range(indx, col):
        #             if board[r][c] != ".":
        #                 tmp_lst.append(board[r][c])
        #     rect_map = Counter(tmp_lst)
        #     if has_repeted_values(values_map=rect_map):
        #         return False

        #     if col == 9:
        #         col = 3
        #         row += 3
        #         row_indx += 3
        #         indx = 0
        #     else:
        #         col += 3
        #         indx += 3

        # return True
