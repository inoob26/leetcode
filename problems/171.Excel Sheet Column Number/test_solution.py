from solution import Solution


def test_solution():
    columnTitle = "A"
    expected = 1
    result = Solution().titleToNumber(columnTitle)
    assert expected == result

    columnTitle = "AB"
    expected = 28
    result = Solution().titleToNumber(columnTitle)
    assert expected == result

    columnTitle = "ZY"
    expected = 701
    result = Solution().titleToNumber(columnTitle)
    assert expected == result

    columnTitle = "BXY"
    expected = 2001
    result = Solution().titleToNumber(columnTitle)
    assert expected == result
