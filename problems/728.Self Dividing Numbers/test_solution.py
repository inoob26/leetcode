from solution import Solution


def test_solution():
    left = 1
    right = 22
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    result = Solution().selfDividingNumbers(left, right)
    assert expected == result

    left = 47
    right = 85
    expected = [48, 55, 66, 77]
    result = Solution().selfDividingNumbers(left, right)
    assert expected == result
