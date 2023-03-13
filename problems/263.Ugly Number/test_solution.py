from solution import Solution


def test_solution():
    n = 6
    expected = True
    result = Solution().isUgly(n)
    assert expected == result

    n = 1
    expected = True
    result = Solution().isUgly(n)
    assert expected == result

    n = 14
    expected = False
    result = Solution().isUgly(n)
    assert expected == result

    n = 8
    expected = True
    result = Solution().isUgly(n)
    assert expected == result
