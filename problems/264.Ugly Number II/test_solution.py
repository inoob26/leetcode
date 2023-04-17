from solution import Solution


def test_solution():
    # n = 10
    # expceted = 12
    # result = Solution().nthUglyNumber(n)
    # assert expceted == result

    # n = 1
    # expceted = 1
    # result = Solution().nthUglyNumber(n)
    # assert expceted == result

    n = 11
    expceted = 15
    result = Solution().nthUglyNumber(n)
    assert expceted == result


test_solution()
