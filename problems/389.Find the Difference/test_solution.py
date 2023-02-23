from solution import Solution


def test_solution():
    s = "abcd"
    t = "abcde"
    expected = "e"
    result = Solution().findTheDifference(s, t)
    assert result == expected
