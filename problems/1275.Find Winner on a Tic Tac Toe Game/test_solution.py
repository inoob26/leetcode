from solution import Solution


def test_solution():
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    expected = "A"
    result = Solution().tictactoe(moves)
    assert expected == result

    moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
    expected = "B"
    result = Solution().tictactoe(moves)
    assert expected == result

    moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    expected = "Draw"
    result = Solution().tictactoe(moves)
    assert expected == result

    moves = [[0, 0], [1, 1]]
    expected = "Pending"
    result = Solution().tictactoe(moves)
    assert expected == result

    moves = [[1, 2], [2, 1], [1, 0], [0, 0], [0, 1], [2, 0], [1, 1]]
    expected = "A"
    result = Solution().tictactoe(moves)
    assert expected == result
