from solution import Solution


def test_solution():
    s = "abc"
    t = "ahbgdc"
    expected = True
    result = Solution().isSubsequence(s, t)
    assert expected == result

    s = "axc"
    t = "ahbgdc"
    expected = False
    result = Solution().isSubsequence(s, t)
    assert expected == result

    s = "acb"
    t = "ahbgdc"
    expected = False
    result = Solution().isSubsequence(s, t)
    assert expected == result

    s = "aaaaaa"
    t = "bbaaaa"
    expected = False
    result = Solution().isSubsequence(s, t)
    assert expected == result

    s = "b"
    t = "abc"
    expected = True
    result = Solution().isSubsequence(s, t)
    assert expected == result
