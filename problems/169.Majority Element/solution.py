from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # v1
        # space O(n)
        # time O(n)
        # num_map = {}
        # for num in nums:
        #     if num not in num_map:
        #         num_map[num] = 1
        #     else:
        #         num_map[num] += 1

        #     if num_map[num] > len(nums) // 2:
        #         return num

        # v2
        # space O(1)
        # time O(n)
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
