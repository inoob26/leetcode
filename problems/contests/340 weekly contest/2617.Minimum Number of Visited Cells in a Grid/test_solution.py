from solution import Solution


def test_solution():
    grid = [[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]]
    expected = 4
    result = Solution().minimumVisitedCells(grid)
    assert expected == result

    grid = [[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]]
    expected = 3
    result = Solution().minimumVisitedCells(grid)
    assert expected == result

    grid = [[2, 1, 0], [1, 0, 0]]
    expected = -1
    result = Solution().minimumVisitedCells(grid)
    assert expected == result

    grid = [
        [2, 1, 1, 1, 1, 2, 2, 1, 0],
        [0, 0, 1, 2, 0, 0, 0, 2, 2],
        [2, 0, 2, 2, 1, 2, 1, 0, 0],
    ]
    expected = 9
    result = Solution().minimumVisitedCells(grid)
    assert expected == result
