from solution import Solution


def test_solution():
    nums = [0, 1, 2, 4, 5, 7]
    expected = ["0->2", "4->5", "7"]
    result = Solution().summaryRanges(nums)
    assert expected == result

    nums = [0, 2, 3, 4, 6, 8, 9]
    expected = ["0", "2->4", "6", "8->9"]
    result = Solution().summaryRanges(nums)
    assert expected == result

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = ["0->9"]
    result = Solution().summaryRanges(nums)
    assert expected == result
