from solution import Solution


def test_solution():
    numRows = 5
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    result = Solution().generate(numRows)
    assert expected == result

    numRows = 1
    expected = [[1]]
    result = Solution().generate(numRows)
    assert expected == result
