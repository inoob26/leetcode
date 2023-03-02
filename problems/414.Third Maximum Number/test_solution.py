from solution import Solution


def test_solution():
    nums = [3, 2, 1]
    expected = 1
    result = Solution().thirdMax(nums)
    assert expected == result

    nums = [1, 2]
    expected = 2
    result = Solution().thirdMax(nums)
    assert expected == result

    nums = [2, 2, 3, 1]
    expected = 1
    result = Solution().thirdMax(nums)
    assert expected == result

    nums = [5, 2, 2]
    expected = 5
    result = Solution().thirdMax(nums)
    assert expected == result

    nums = [1, 2, 2, 5, 3, 5]
    expected = 2
    result = Solution().thirdMax(nums)
    assert expected == result
