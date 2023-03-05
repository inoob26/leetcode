from solution import Solution


def test_solution():
    heights = [1, 1, 4, 2, 1, 3]
    expected = 3
    result = Solution().heightChecker(heights)
    assert expected == result

    heights = [5, 1, 2, 3, 4]
    expected = 5
    result = Solution().heightChecker(heights)
    assert expected == result

    heights = [1, 2, 3, 4, 5]
    expected = 0
    result = Solution().heightChecker(heights)
    assert expected == result
