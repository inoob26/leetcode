from solution import Solution


def test_solution():
    moves = "LL"
    expected = False
    result = Solution().judgeCircle(moves)
    assert expected == result

    moves = "UD"
    expected = True
    result = Solution().judgeCircle(moves)
    assert expected == result
