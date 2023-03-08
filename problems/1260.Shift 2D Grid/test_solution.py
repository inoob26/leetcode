from solution import Solution


def test_solution():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    expected = [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
    result = Solution().shiftGrid(grid, k)
    assert expected == result

    grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k = 4
    expected = [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]
    result = Solution().shiftGrid(grid, k)
    assert expected == result

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 9
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = Solution().shiftGrid(grid, k)
    assert expected == result


test_solution()
