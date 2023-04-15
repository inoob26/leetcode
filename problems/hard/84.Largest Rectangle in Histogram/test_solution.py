from solution import Solution


def test_solution():
    heights = [2, 1, 5, 6, 2, 3]
    expected = 10
    result = Solution().largestRectangleArea(heights)
    assert expected == result

    heights = [2, 4]
    expected = 4
    result = Solution().largestRectangleArea(heights)
    assert expected == result
