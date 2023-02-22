from solution import Solution


def test_solution():
    ransomNote = "a"
    magazine = "b"
    expected = False
    result = Solution().canConstruct(ransomNote, magazine)
    assert expected == result

    ransomNote = "aa"
    magazine = "ab"
    expected = False
    result = Solution().canConstruct(ransomNote, magazine)
    assert expected == result

    ransomNote = "aa"
    magazine = "aab"
    expected = True
    result = Solution().canConstruct(ransomNote, magazine)
    assert expected == result

    ransomNote = "aab"
    magazine = "baa"
    expected = True
    result = Solution().canConstruct(ransomNote, magazine)
    assert expected == result

    ransomNote = "fffbfg"
    magazine = "effjfggbffjdgbjjhhdegh"
    expected = True
    result = Solution().canConstruct(ransomNote, magazine)
    assert expected == result
