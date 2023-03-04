from solution import Solution


def test_solution():
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    expected = 5
    result = Solution().findLHS(nums)
    assert expected == result

    nums = [1, 2, 3, 4]
    expected = 2
    result = Solution().findLHS(nums)
    assert expected == result

    nums = [1, 1, 1, 1]
    expected = 0
    result = Solution().findLHS(nums)
    assert expected == result
