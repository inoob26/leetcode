from solution import Solution


def test_solution():
    s = "A man, a plan, a canal: Panama"
    expected = True
    result = Solution().isPalindrome(s)
    assert expected == result

    s = "race a car"
    expected = False
    result = Solution().isPalindrome(s)
    assert expected == result

    s = " "
    expected = True
    result = Solution().isPalindrome(s)
    assert expected == result

    s = "0P"
    expected = False
    result = Solution().isPalindrome(s)
    assert expected == result
