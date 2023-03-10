from solution import Solution


def test_solution():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]
    result = Solution().merge(nums1, m, nums2, n)
    assert expected == result

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    expected = [1]
    result = Solution().merge(nums1, m, nums2, n)
    assert expected == result

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    expected = [1]
    result = Solution().merge(nums1, m, nums2, n)
    assert expected == result
