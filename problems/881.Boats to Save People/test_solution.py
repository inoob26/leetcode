from solution import Solution


def test_solution():
    people = [1, 2]
    limit = 3
    expected = 1
    result = Solution().numRescueBoats(people, limit)
    assert expected == result

    people = [3, 2, 2, 1]
    limit = 3
    expected = 3
    result = Solution().numRescueBoats(people, limit)
    assert expected == result

    people = [3, 5, 3, 4]
    limit = 5
    expected = 4
    result = Solution().numRescueBoats(people, limit)
    assert expected == result
