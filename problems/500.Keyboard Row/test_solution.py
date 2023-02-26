from solution import Solution


def test_solution():
    words = ["Hello", "Alaska", "Dad", "Peace"]
    expected = ["Alaska", "Dad"]
    result = Solution().findWords(words)
    assert expected == result

    words = words = ["omk"]
    expected = []
    result = Solution().findWords(words)
    assert expected == result

    words = ["adsdf", "sfd"]
    expected = ["adsdf", "sfd"]
    result = Solution().findWords(words)
    assert expected == result
