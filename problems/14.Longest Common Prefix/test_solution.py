from solution import Solution


def test_solution():
    strs = ["flower", "flow", "flight"]
    expected = "fl"
    result = Solution().longestCommonPrefix(strs)
    assert result == expected

    strs = ["dog", "racecar", "car"]
    expected = ""
    result = Solution().longestCommonPrefix(strs)
    assert result == expected

    strs = ["a"]
    expected = "a"
    result = Solution().longestCommonPrefix(strs)
    assert result == expected
