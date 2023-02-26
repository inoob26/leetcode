from solution import Solution

def test_solution():
    s = "Let's take LeetCode contest"
    expected = "s'teL ekat edoCteeL tsetnoc"
    result = Solution().reverseWords(s)
    assert expected == result

    s = "God Ding"
    expected = "doG gniD"
    result = Solution().reverseWords(s)
    assert expected == result