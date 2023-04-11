from solution import Solution


def test_solution():
    nums = [10, 1, 2, 7, 1, 3]
    p = 2
    expected = 1
    result = Solution().minimizeMax(nums, p)
    assert expected == result

    nums = [4, 2, 1, 2]
    p = 1
    expected = 0
    result = Solution().minimizeMax(nums, p)
    assert expected == result

    nums = [4, 2, 1, 2]
    p = 0
    expected = 0
    result = Solution().minimizeMax(nums, p)
    assert expected == result
