from solution import Solution


def test_solution():
    x = 121
    expected = 11
    result = Solution().mySqrt(x)
    assert expected == result
