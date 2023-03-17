from solution import Solution


def test_solution():
    num = 38
    expected = 2
    result = Solution().addDigits(num)
    assert expected == result

    num = 0
    expected = 0
    result = Solution().addDigits(num)
    assert expected == result

    num = 10
    expected = 1
    result = Solution().addDigits(num)
    assert expected == result
