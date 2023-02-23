from solution import Solution


def test_solution():
    s = "leetcode"
    expected = 0
    result = Solution().firstUniqChar(s)
    assert result == expected

    s = "loveleetcode"
    expected = 2
    result = Solution().firstUniqChar(s)
    assert result == expected

    s = "aabb"
    expected = -1
    result = Solution().firstUniqChar(s)
    assert result == expected
