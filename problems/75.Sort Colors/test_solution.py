from solution import Solution


def test_solution():
    nums = [2, 0, 2, 1, 1, 0]
    expected = [0, 0, 1, 1, 2, 2]
    Solution().sortColors(nums)
    assert expected == nums

    nums = [2, 0, 1]
    expected = [0, 1, 2]
    Solution().sortColors(nums)
    assert expected == nums


# test_solution()
