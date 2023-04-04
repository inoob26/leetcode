from solution import Solution


def test_solution():
    s = "abacaba"
    expected = 4
    result = Solution().partitionString(s)
    assert expected == result

    s = "ssssss"
    expected = 6
    result = Solution().partitionString(s)
    assert expected == result

    s = "cuieokbs"
    expected = 1
    result = Solution().partitionString(s)
    assert expected == result
