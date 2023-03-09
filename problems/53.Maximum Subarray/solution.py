from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum = max(0, curr_sum) + num
            result = max(curr_sum, result)

        return result

        # dynamic programming
        # size = len(nums)

        # dp = [0] * size
        # dp[0] = nums[0]

        # for i in range(1, size):
        #     dp[i] = max(nums[i], nums[i] + dp[i-1])
        # return max(dp)
