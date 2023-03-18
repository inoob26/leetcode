from solution import Solution


def test_solution():
    nums = [1, 3]
    expected = 6
    result = Solution().subsetXORSum(nums)
    assert expected == result

    nums = [5, 1, 6]
    expected = 28
    result = Solution().subsetXORSum(nums)
    assert expected == result

    nums = [3, 4, 5, 6, 7, 8]
    expected = 480
    result = Solution().subsetXORSum(nums)
    assert expected == result
