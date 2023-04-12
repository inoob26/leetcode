from solution import Solution


def test_solution():
    path = "/a/b//c/.././d/../f"
    expected = "/a/b/f"
    result = Solution().simplifyPath(path)
    assert expected == result

    path = "/home/"
    expected = "/home"
    result = Solution().simplifyPath(path)
    assert expected == result

    path = "/../"
    expected = "/"
    result = Solution().simplifyPath(path)
    assert expected == result

    path = "/home//foo/"
    expected = "/home/foo"
    result = Solution().simplifyPath(path)
    assert expected == result

    path = "/a/../../b/../c//.//"
    expected = "/c"
    result = Solution().simplifyPath(path)
    assert expected == result


test_solution()
