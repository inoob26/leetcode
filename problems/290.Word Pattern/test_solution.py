from solution import Solution


def test_solution():
    pattern = "abba"
    s = "dog cat cat dog"
    expected = True
    result = Solution().wordPattern(pattern, s)
    assert expected == result

    pattern = "abba"
    s = "dog cat cat fish"
    expected = False
    result = Solution().wordPattern(pattern, s)
    assert expected == result

    pattern = "aaaa"
    s = "dog cat cat dog"
    expected = False
    result = Solution().wordPattern(pattern, s)
    assert expected == result

    pattern = "abba"
    s = "dog dog dog dog"
    expected = False
    result = Solution().wordPattern(pattern, s)
    assert expected == result

    pattern = "aaa"
    s = "aa aa aa aa"
    expected = False
    result = Solution().wordPattern(pattern, s)
    assert expected == result
