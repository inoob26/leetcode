from solution import Solution


def test_solution():
    nums = [5, 2, 3, 1]
    expected = [1, 2, 3, 5]
    result = Solution().sortArray(nums)
    assert expected == result

    nums = [5, 1, 1, 2, 0, 0]
    expected = [0, 0, 1, 1, 2, 5]
    result = Solution().sortArray(nums)
    assert expected == result
