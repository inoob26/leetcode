from solution import Solution


def test_solution():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    expected = True
    result = Solution().searchMatrix(matrix, target)
    assert expected == result

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    expected = False
    result = Solution().searchMatrix(matrix, target)
    assert expected == result

    matrix = [[1]]
    target = 1
    expected = True
    result = Solution().searchMatrix(matrix, target)
    assert expected == result

    matrix = [[1, 3]]
    target = 3
    expected = True
    result = Solution().searchMatrix(matrix, target)
    assert expected == result
