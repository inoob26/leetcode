from solution import Solution


def test_solution():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    expected = [2, 2]
    result = Solution().intersect(nums1, nums2)
    assert expected == result

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    expected = [4, 9]
    result = Solution().intersect(nums1, nums2)
    assert expected == result

    nums1 = [70, 72, 63, 56, 5, 33, 51, 65, 41, 10, 23]
    nums2 = [
        40,
        99,
        62,
        84,
        77,
        21,
        0,
        19,
        35,
        42,
        75,
        46,
        96,
        14,
        65,
        6,
        47,
        16,
        39,
        1,
        97,
        96,
        10,
        29,
        55,
        72,
        87,
        81,
        53,
        74,
        3,
        13,
        20,
        35,
        99,
        10,
        19,
        48,
        72,
        37,
        83,
        41,
        99,
        81,
        37,
        20,
        96,
        78,
        95,
        70,
        45,
        37,
        3,
        29,
    ]
    expected = [10, 41, 65, 70, 72]
    result = Solution().intersect(nums1, nums2)
    assert expected == result
