from solution import Solution

# get max and min
# if min index less than max index
# return max value - min value
# else 0


def test_solution():
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5
    result = Solution().maxProfit(prices)
    assert expected == result

    prices = [7, 6, 4, 3, 1]
    expected = 0
    result = Solution().maxProfit(prices)
    assert expected == result

    prices = [1, 2]
    expected = 1
    result = Solution().maxProfit(prices)
    assert expected == result
