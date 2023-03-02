from solution import Solution


def test_solution():
    nums = [1, 1, 0, 1, 1, 1]
    expected = 3
    result = Solution().findMaxConsecutiveOnes(nums)
    assert expected == result

    # nums = [1, 0, 1, 1, 0, 1]
    # expected = 2
    # result = Solution().findMaxConsecutiveOnes(nums)
    # assert expected == result


test_solution()
