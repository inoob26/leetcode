from solution import Solution


def test_solution():
    nums = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
    expected = 11
    result = Solution().diagonalPrime(nums)
    assert expected == result

    nums = [[1, 2, 3], [5, 17, 7], [9, 11, 10]]
    expected = 17
    result = Solution().diagonalPrime(nums)
    assert expected == result
