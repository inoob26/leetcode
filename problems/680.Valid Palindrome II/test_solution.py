from solution import Solution


def test_solution():
    s = "aba"
    expected = True
    result = Solution().validPalindrome(s)
    assert expected == result

    s = "abca"
    expected = True
    result = Solution().validPalindrome(s)
    assert expected == result

    s = "abc"
    expected = False
    result = Solution().validPalindrome(s)
    assert expected == result

    s = "deeee"
    expected = True
    result = Solution().validPalindrome(s)
    assert expected == result

    s = "cbbcc"
    expected = True
    result = Solution().validPalindrome(s)
    assert expected == result

    s = "bebeb"
    expected = True
    result = Solution().validPalindrome(s)
    assert expected == result
