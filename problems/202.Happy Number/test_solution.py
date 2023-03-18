from solution import Solution


def test_solution():
    n = 19
    expected = True
    result = Solution().isHappy(n)
    assert expected == result

    n = 2
    expected = False
    result = Solution().isHappy(n)
    assert expected == result

    n = 7
    expected = True
    result = Solution().isHappy(n)
    assert expected == result
