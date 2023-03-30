from solution import Solution


def test_solution():
    num = 100
    expected = "202"
    result = Solution().convertToBase7(num)
    assert expected == result

    num = -7
    expected = "-10"
    result = Solution().convertToBase7(num)
    assert expected == result

    num = 0
    expected = "0"
    result = Solution().convertToBase7(num)
    assert expected == result


test_solution()
