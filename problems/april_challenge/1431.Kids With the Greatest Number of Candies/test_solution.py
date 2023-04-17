from solution import Solution


def test_solution():
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    expected = [True, True, True, False, True]
    result = Solution().kidsWithCandies(candies, extraCandies)
    assert expected == result

    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    expected = [True, False, False, False, False]
    result = Solution().kidsWithCandies(candies, extraCandies)
    assert expected == result
