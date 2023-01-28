from solution import Solution


def test_solution():
    nums = [1, 7, 3, 6, 5, 6]
    expected = 3
    result = Solution().pivotIndex(nums)
    assert result == expected

    nums = [1, 2, 3]
    expected = -1
    result = Solution().pivotIndex(nums)
    assert result == expected

    nums = [2, 1, -1]
    expected = 0
    result = Solution().pivotIndex(nums)
    assert result == expected
