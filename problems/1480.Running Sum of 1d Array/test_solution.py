from solution import Solution


def test_solution():
    nums = [1, 2, 3, 4]
    expected = [1, 3, 6, 10]
    result = Solution().runningSum(nums)
    assert expected == result

    nums = [1, 1, 1, 1, 1]
    expected = [1, 2, 3, 4, 5]
    result = Solution().runningSum(nums)
    assert expected == result

    nums = [3, 1, 2, 10, 1]
    expected = [3, 4, 6, 16, 17]
    result = Solution().runningSum(nums)
    assert expected == result
