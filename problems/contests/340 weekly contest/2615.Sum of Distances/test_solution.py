from solution import Solution


def test_solution():
    nums = [1, 3, 1, 1, 2]
    expected = [5, 0, 3, 4, 0]
    result = Solution().distance(nums)
    assert expected == result

    nums = [0, 5, 3]
    expected = [0, 0, 0]
    result = Solution().distance(nums)
    assert expected == result
