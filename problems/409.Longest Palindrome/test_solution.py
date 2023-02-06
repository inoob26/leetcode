from solution import Solution


def test_solution():
    s = "abccccdd"
    expected = 7
    result = Solution().longestPalindrome(s)
    assert expected == result

    s = "a"
    expected = 1
    result = Solution().longestPalindrome(s)
    assert expected == result
