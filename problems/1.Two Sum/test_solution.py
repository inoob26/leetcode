from solution import Solution


def test_solution():
    nums = [2, 7, 11, 15]
    target = 9

    expected_output = [0, 1]
    expected_output_2 = [1, 0]
    output = Solution().twoSum(nums, target)
    assert expected_output == output or expected_output_2 == output

    nums = [3, 2, 4]
    target = 6

    expected_output = [1, 2]
    expected_output_2 = [2, 1]
    output = Solution().twoSum(nums, target)
    assert expected_output == output or expected_output_2 == output

    nums = [3, 3]
    target = 6

    expected_output = [0, 1]
    expected_output_2 = [1, 0]
    output = Solution().twoSum(nums, target)
    assert expected_output == output or expected_output_2 == output

    nums = [3, 2, 3]
    target = 6

    expected_output = [0, 2]
    expected_output_2 = [2, 0]
    output = Solution().twoSum(nums, target)
    assert expected_output == output or expected_output_2 == output
