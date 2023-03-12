from solution import Solution


def test_solution():
    columnNumber = 1
    expected = "A"
    result = Solution().convertToTitle(columnNumber)
    assert expected == result

    columnNumber = 28
    expected = "AB"
    result = Solution().convertToTitle(columnNumber)
    assert expected == result

    columnNumber = 701
    expected = "ZY"
    result = Solution().convertToTitle(columnNumber)
    assert expected == result

    columnNumber = 2001
    expected = "BXY"
    result = Solution().convertToTitle(columnNumber)
    assert expected == result
