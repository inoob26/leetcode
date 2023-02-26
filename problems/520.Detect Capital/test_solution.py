from solution import Solution


def test_solution():
    word = "USA"
    expected = True
    result = Solution().detectCapitalUse(word)
    assert expected == result

    word = "FlaG"
    expected = False
    result = Solution().detectCapitalUse(word)
    assert expected == result
