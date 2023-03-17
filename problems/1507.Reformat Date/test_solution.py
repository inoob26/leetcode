from solution import Solution


def test_solution():
    date = "20th Oct 2052"
    expected = "2052-10-20"
    result = Solution().reformatDate(date)
    assert expected == result

    date = "6th Jun 1933"
    expected = "1933-06-06"
    result = Solution().reformatDate(date)
    assert expected == result

    date = "26th May 1960"
    expected = "1960-05-26"
    result = Solution().reformatDate(date)
    assert expected == result
