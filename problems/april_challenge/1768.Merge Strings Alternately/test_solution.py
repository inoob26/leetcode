from solution import Solution


def test_solution():
    word1 = "abc"
    word2 = "pqr"
    expected = "apbqcr"
    result = Solution().mergeAlternately(word1, word2)
    assert expected == result

    word1 = "ab"
    word2 = "pqrs"
    expected = "apbqrs"
    result = Solution().mergeAlternately(word1, word2)
    assert expected == result

    word1 = "abcd"
    word2 = "pq"
    expected = "apbqcd"
    result = Solution().mergeAlternately(word1, word2)
    assert expected == result
