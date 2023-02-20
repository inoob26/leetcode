from solution import Solution


def test_solution():
    s = "Hello World"
    expected = 5
    result = Solution().lengthOfLastWord(s)
    assert result == expected

    s = "   fly me   to   the moon  "
    expected = 4
    result = Solution().lengthOfLastWord(s)
    assert result == expected

    s = "luffy is still joyboy"
    expected = 6
    result = Solution().lengthOfLastWord(s)
    assert result == expected
