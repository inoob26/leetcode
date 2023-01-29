from solution import Solution


def test_solution():
    s = "egg"
    t = "add"
    expected = True
    result = Solution().isIsomorphic(s, t)
    assert expected == result

    s = "foo"
    t = "bar"
    expected = False
    result = Solution().isIsomorphic(s, t)
    assert expected == result

    s = "paper"
    t = "title"
    expected = True
    result = Solution().isIsomorphic(s, t)
    assert expected == result

    s = "badc"
    t = "baba"
    expected = False
    result = Solution().isIsomorphic(s, t)
    assert expected == result

    s = "bbbaaaba"
    t = "aaabbbba"
    expected = False
    result = Solution().isIsomorphic(s, t)
    assert expected == result
