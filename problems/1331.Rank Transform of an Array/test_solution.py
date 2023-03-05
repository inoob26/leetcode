from solution import Solution


def test_solution():
    arr = [40, 10, 20, 30]
    expected = [4, 1, 2, 3]
    result = Solution().arrayRankTransform(arr)
    assert expected == result

    arr = [100, 100, 100]
    expected = [1, 1, 1]
    result = Solution().arrayRankTransform(arr)
    assert expected == result

    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    expected = [5, 3, 4, 2, 8, 6, 7, 1, 3]
    result = Solution().arrayRankTransform(arr)
    assert expected == result
