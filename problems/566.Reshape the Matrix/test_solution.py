from solution import Solution


def test_solution():
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    expected = [[1, 2, 3, 4]]
    result = Solution().matrixReshape(mat, r, c)
    assert expected == result

    mat = [[1, 2], [3, 4]]
    r = 2
    c = 4
    expected = [[1, 2], [3, 4]]
    result = Solution().matrixReshape(mat, r, c)
    assert expected == result
