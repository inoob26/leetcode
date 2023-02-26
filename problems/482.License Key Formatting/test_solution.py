from solution import Solution


def test_solution():

    s = "5F3Z-2e-9-w"
    k = 4
    expected = "5F3Z-2E9W"
    result = Solution().licenseKeyFormatting(s, k)
    assert expected == result

    s = "2-5g-3-J"
    k = 2
    expected = "2-5G-3J"
    result = Solution().licenseKeyFormatting(s, k)
    assert expected == result


def test_logn_license_key():
    s = "asdddwas21e-we3ecc-w"
    k = 3
    expected = "ASD-DDW-AS2-1EW-E3E-CCW"
    result = Solution().licenseKeyFormatting(s, k)
    assert expected == result
