from solution import Solution


def test_solution():
    score = [5, 4, 3, 2, 1]
    expected = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    result = Solution().findRelativeRanks(score)
    assert expected == result

    score = [10, 3, 8, 9, 4]
    expected = ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
    result = Solution().findRelativeRanks(score)
    assert expected == result
