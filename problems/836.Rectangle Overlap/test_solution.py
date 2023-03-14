from solution import Solution


def test_solution():
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    expected = True
    result = Solution().isRectangleOverlap(rec1, rec2)
    assert expected == result

    rec1 = [0, 0, 1, 1]
    rec2 = [1, 0, 2, 1]
    expected = False
    result = Solution().isRectangleOverlap(rec1, rec2)
    assert expected == result

    rec1 = [0, 0, 1, 1]
    rec2 = [2, 2, 3, 3]
    expected = False
    result = Solution().isRectangleOverlap(rec1, rec2)
    assert expected == result

    rec1 = [-382, -696, 838, -517]
    rec2 = [-110, -690, 247, -209]
    expected = True
    result = Solution().isRectangleOverlap(rec1, rec2)
    assert expected == result
