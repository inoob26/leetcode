from solution import Solution


def test_solution():
    digits = [1, 2, 3]
    expected = [1, 2, 4]
    result = Solution().plusOne(digits)
    assert expected == result

    digits = [4, 3, 2, 1]
    expected = [4, 3, 2, 2]
    result = Solution().plusOne(digits)
    assert expected == result

    digits = [9]
    expected = [1, 0]
    result = Solution().plusOne(digits)
    assert expected == result

    digits = [4, 3, 9, 9]
    expected = [4, 4, 0, 0]
    result = Solution().plusOne(digits)
    assert expected == result

    digits = [4, 9, 9, 9]
    expected = [5, 0, 0, 0]
    result = Solution().plusOne(digits)
    assert expected == result

    digits = [9, 9, 9, 9]
    expected = [1, 0, 0, 0, 0]
    result = Solution().plusOne(digits)
    assert expected == result
