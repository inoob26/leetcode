from solution import Solution


def test_solution():
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    expected = 16
    result = Solution().islandPerimeter(grid)
    assert expected == result

    grid = [[1]]
    expected = 4
    result = Solution().islandPerimeter(grid)
    assert expected == result

    grid = [[1, 0]]
    expected = 4
    result = Solution().islandPerimeter(grid)
    assert expected == result

    grid = [[0], [1], [1]]
    expected = 6
    result = Solution().islandPerimeter(grid)
    assert expected == result
