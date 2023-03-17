from solution import Solution


def test_solution():
    day = 31
    month = 8
    year = 2019
    expected = "Saturday"
    result = Solution().dayOfTheWeek(day, month, year)
    assert expected == result

    day = 18
    month = 7
    year = 1999
    expected = "Sunday"
    result = Solution().dayOfTheWeek(day, month, year)
    assert expected == result

    day = 15
    month = 8
    year = 1993
    expected = "Sunday"
    result = Solution().dayOfTheWeek(day, month, year)
    assert expected == result
