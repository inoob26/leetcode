from solution import Solution


def test_solution():
    nums = [1, 2, 2, 3, 1]
    expected = 2
    result = Solution().findShortestSubArray(nums)
    assert expected == result

    nums = [1, 2, 2, 3, 1, 4, 2]
    expected = 6
    result = Solution().findShortestSubArray(nums)
    assert expected == result

    nums = [1, 2, 2, 4, 2, 3]  # [2,2,4,2]
    expected = 4
    result = Solution().findShortestSubArray(nums)
    assert expected == result

    nums = [1, 5, 2, 3, 5, 4, 5, 6]  # [5, 2, 3, 5, 4, 5]
    expected = 6
    result = Solution().findShortestSubArray(nums)
    assert expected == result
