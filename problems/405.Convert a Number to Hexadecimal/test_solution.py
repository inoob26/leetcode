from solution import Solution


def test_solution():
    num = 26
    expected = "1a"
    result = Solution().toHex(num)
    assert expected == result

    num = -1
    expected = "ffffffff"
    result = Solution().toHex(num)
    assert expected == result


test_solution()
