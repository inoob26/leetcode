from solution import Solution


def test_solution():
    candyType = [1, 1, 2, 2, 3, 3]
    expected = 3
    result = Solution().distributeCandies(candyType)
    assert expected == result

    candyType = [1, 1, 2, 3]
    expected = 2
    result = Solution().distributeCandies(candyType)
    assert expected == result

    candyType = [6, 6, 6, 6]
    expected = 1
    result = Solution().distributeCandies(candyType)
    assert expected == result
