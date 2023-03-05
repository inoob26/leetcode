from solution import Solution


def test_solution():
    nums = [3, 6, 1, 0]
    expected = 1
    result = Solution().dominantIndex(nums)
    assert expected == result

    nums = [1, 2, 3, 4]
    expected = -1
    result = Solution().dominantIndex(nums)
    assert expected == result

    nums = [0, 0, 0, 1]
    expected = 3
    result = Solution().dominantIndex(nums)
    assert expected == result

    nums = [1, 0]
    expected = 0
    result = Solution().dominantIndex(nums)
    assert expected == result
