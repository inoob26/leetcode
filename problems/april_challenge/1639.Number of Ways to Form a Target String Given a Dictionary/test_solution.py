from solution import Solution


def test_solution():
    words = ["acca", "bbbb", "caca"]
    target = "aba"
    expected = 6
    result = Solution().numWays(words, target)
    assert expected == result

    words = ["abba", "baab"]
    target = "bab"
    expected = 4
    result = Solution().numWays(words, target)
    assert expected == result
