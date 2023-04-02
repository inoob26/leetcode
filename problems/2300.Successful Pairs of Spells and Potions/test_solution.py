from solution import Solution


def test_solution():
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7

    expected = [4, 0, 3]
    result = Solution().successfulPairs(spells, potions, success)
    assert expected == result

    spells = [3, 1, 2]
    potions = [8, 5, 8]
    success = 16

    expected = [2, 0, 2]
    result = Solution().successfulPairs(spells, potions, success)
    assert expected == result
