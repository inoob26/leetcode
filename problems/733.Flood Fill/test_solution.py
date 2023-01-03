from solution import Solution


def test_solution():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    result = Solution().floodFill(image, sr, sc, color)
    assert expected == result

    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    color = 0
    expected = [[0, 0, 0], [0, 0, 0]]
    result = Solution().floodFill(image, sr, sc, color)
    assert expected == result
