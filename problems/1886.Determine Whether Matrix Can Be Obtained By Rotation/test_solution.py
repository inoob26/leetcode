from solution import Solution


def test_solution():
    mat = [[0, 1], [1, 0]]
    target = [[1, 0], [0, 1]]
    expected = True
    result = Solution().findRotation(mat, target)
    assert expected == result

    mat = [[0, 1], [1, 1]]
    target = [[1, 0], [0, 1]]
    expected = False
    result = Solution().findRotation(mat, target)
    assert expected == result

    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    expected = True
    result = Solution().findRotation(mat, target)
    assert expected == result
