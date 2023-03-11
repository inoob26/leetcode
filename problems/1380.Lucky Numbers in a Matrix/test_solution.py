from solution import Solution


def test_solution():
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    expected = [15]
    result = Solution().luckyNumbers(matrix)
    assert expected == result

    matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    expected = [12]
    result = Solution().luckyNumbers(matrix)
    assert expected == result

    matrix = [[7, 8], [1, 2]]
    expected = [7]
    result = Solution().luckyNumbers(matrix)
    assert expected == result
