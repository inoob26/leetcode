from solution import Solution


def test_solution():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    expected = 4
    result = Solution().search(nums, target)
    assert expected == result

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    expected = -1
    result = Solution().search(nums, target)
    assert expected == result

    nums = [5]
    target = 5
    expected = 0
    result = Solution().search(nums, target)
    assert expected == result

    nums = [2, 5]
    target = 5
    expected = 1
    result = Solution().search(nums, target)
    assert expected == result
