from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # second approach
        size = 3
        rows, cols = [0] * size, [0] * size
        diagonal = antidiagonal = 0

        player = 1
        for row, col in moves:
            rows[row] += player
            cols[col] += player

            if row == col:
                diagonal += player
            if row + col == size - 1:
                antidiagonal += player

            if any(
                abs(line) == size
                for line in (rows[row], cols[col], diagonal, antidiagonal)
            ):
                return "A" if player == 1 else "B"

            player *= -1
        return "Draw" if len(moves) == size * size else "Pending"

        # first approach
        # size = 3
        # board = [[0] * size for _ in range(size)]

        # def check_row(row, player_id):
        #     for col in range(size):
        #         if board[row][col] != player_id:
        #             return False
        #     return True

        # def check_col(col, player_id):
        #     for row in range(size):
        #         if board[row][col] != player_id:
        #             return False
        #     return True

        # def check_diagonal(player_id):
        #     for row in range(size):
        #         if board[row][row] != player_id:
        #             return False
        #     return True

        # def check_antidiagonal(player_id):
        #     for row in range(size):
        #         if board[row][size - 1 - row] != player_id:
        #             return False
        #     return True

        # player = 1
        # for move in moves:
        #     row, col = move
        #     board[row][col] = player

        #     if (
        #         check_row(row, player)
        #         or check_col(col, player)
        #         or (row == col and check_diagonal(player))
        #         or (row + col == size - 1 and check_antidiagonal(player))
        #     ):
        #         return "A" if player == 1 else "B"

        #     player *= -1

        # return "Draw" if len(moves) == size * size else "Pending"

        # my solution
        # win_map = [
        #     [[0, 0], [0, 1], [0, 2]],
        #     [[0, 1], [1, 1], [2, 1]],
        #     [[0, 2], [1, 2], [2, 2]],
        #     [[0, 0], [1, 1], [2, 2]],
        #     [[0, 2], [1, 1], [2, 0]],
        #     [[0, 0], [0, 1], [0, 2]],
        #     [[1, 0], [1, 1], [1, 2]],
        #     [[2, 0], [2, 1], [2, 2]],
        # ]
        # # [[2, 0], [0, 0], [2, 1], [2, 2]]

        # a_moves = []
        # b_moves = []
        # for indx, val in enumerate(moves):
        #     if indx % 2 == 0:
        #         a_moves.append(val)
        #     else:
        #         b_moves.append(val)

        # if sorted(a_moves) in win_map:
        #     winer = "A"
        # elif sorted(b_moves) in win_map:
        #     winer = "B"
        # elif len(moves) == 9:
        #     return "Draw"
        # else:
        #     return "Pending"

        # return winer
