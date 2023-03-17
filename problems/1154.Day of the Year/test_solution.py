from solution import Solution


def test_solution():
    date = "2019-01-09"
    expected = 9
    result = Solution().dayOfYear(date)
    assert expected == result

    date = "2019-02-10"
    expected = 41
    result = Solution().dayOfYear(date)
    assert expected == result
