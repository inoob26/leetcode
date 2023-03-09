from solution import Solution


def test_solution():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    result = Solution().maxSubArray(nums)
    assert expected == result

    nums = [1]
    expected = 1
    result = Solution().maxSubArray(nums)
    assert expected == result

    nums = [5, 4, -1, 7, 8]
    expected = 23
    result = Solution().maxSubArray(nums)
    assert expected == result
