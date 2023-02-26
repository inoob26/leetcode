from solution import Solution


def test_solution():
    s = "PPALLP"
    expected = True
    result = Solution().checkRecord(s)
    assert expected == result

    s = "PPALLL"
    expected = False
    result = Solution().checkRecord(s)
    assert expected == result


test_solution()
