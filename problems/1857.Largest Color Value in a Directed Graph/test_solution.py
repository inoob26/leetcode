from solution import Solution


def test_solution():
    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
    expected = 3
    result = Solution().largestPathValue(colors, edges)
    assert expected == result

    colors = "a"
    edges = [[0, 0]]
    expected = -1
    result = Solution().largestPathValue(colors, edges)
    assert expected == result

    colors = "hhqhuqhqff"
    edges = [
        [0, 1],
        [0, 2],
        [2, 3],
        [3, 4],
        [3, 5],
        [5, 6],
        [2, 7],
        [6, 7],
        [7, 8],
        [3, 8],
        [5, 8],
        [8, 9],
        [3, 9],
        [6, 9],
    ]
    expected = 3
    result = Solution().largestPathValue(colors, edges)
    assert expected == result


test_solution()
