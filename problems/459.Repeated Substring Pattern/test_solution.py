from solution import Solution


def test_solution():
    s = "abab"
    expected = True
    result = Solution().repeatedSubstringPattern(s)
    assert result == expected

    s = "aba"
    expected = False
    result = Solution().repeatedSubstringPattern(s)
    assert result == expected

    s = "abcabcabcabc"
    expected = True
    result = Solution().repeatedSubstringPattern(s)
    assert result == expected

    s = "abac"
    expected = False
    result = Solution().repeatedSubstringPattern(s)
    assert result == expected

    s = "ababba"
    expected = False
    result = Solution().repeatedSubstringPattern(s)
    assert result == expected

    s = "abaababaab"
    expected = True
    result = Solution().repeatedSubstringPattern(s)
    assert result == expected
