from solution import Solution


def test_solution():
    s = "abcdefg"
    k = 2
    expected = "bacdfeg"
    result = Solution().reverseStr(s, k)
    assert expected == result

    s = "abcd"
    k = 2
    expected = "bacd"
    result = Solution().reverseStr(s, k)
    assert expected == result

    s = "abc"
    k = 2
    expected = "bac"
    result = Solution().reverseStr(s, k)
    assert expected == result
