from solution import Solution


def test_solution():
    nums = [1, 2, 3]
    expected = 6
    result = Solution().maximumProduct(nums)
    assert expected == result

    nums = [1, 2, 3, 4]
    expected = 24
    result = Solution().maximumProduct(nums)
    assert expected == result

    nums = [-1, -2, -3]
    expected = -6
    result = Solution().maximumProduct(nums)
    assert expected == result

    nums = [-100, -98, -1, 2, 3, 4]
    expected = 39200
    result = Solution().maximumProduct(nums)
    assert expected == result

    nums = [-100, -2, -3, 1]
    expected = 300
    result = Solution().maximumProduct(nums)
    assert expected == result


test_solution()
