from solution import Solution


def test_solution():
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    result = Solution().productExceptSelf(nums)
    assert expected == result


test_solution()
