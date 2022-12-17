from solution import Solution


def test_solution():
    s = "()"
    expected = True
    result = Solution().isValid(s)
    assert expected == result

    s = "()[]{}"
    expected = True
    result = Solution().isValid(s)
    assert expected == result

    s = "(]"
    expected = False
    result = Solution().isValid(s)
    assert expected == result

    s = "]"
    expected = False
    result = Solution().isValid(s)
    assert expected == result
