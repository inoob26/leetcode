from solution import Solution


def test_solution():
    s = ""
    t = ""
    expected = True

    result = Solution().isAnagram(s, t)
    assert expected == result

    s = "anagram"
    t = "nagaram"
    expected = True

    result = Solution().isAnagram(s, t)
    assert expected == result

    s = "rat"
    t = "car"
    expected = False

    result = Solution().isAnagram(s, t)
    assert expected == result

    s = "rt"
    t = "car"
    expected = False
    result = Solution().isAnagram(s, t)
    assert expected == result
