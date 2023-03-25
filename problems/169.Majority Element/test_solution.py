from solution import Solution


def test_solution():
    nums = [3, 2, 3]
    expected = 3
    result = Solution().majorityElement(nums)
    assert expected == result

    nums = [2, 2, 1, 1, 1, 2, 2]
    expected = 2
    result = Solution().majorityElement(nums)
    assert expected == result
