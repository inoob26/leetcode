from typing import List
from collections import defaultdict


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # v2 not my idea
        size = len(nums)
        result = [0 for _ in range(size)]
        seen_with_sum = defaultdict(int)
        count_map = defaultdict(int)

        # left to right
        for indx in range(size):
            # 2*i - (j1 + j2)
            result[indx] += (count_map[nums[indx]] * indx) - seen_with_sum[nums[indx]]
            seen_with_sum[nums[indx]] += indx
            count_map[nums[indx]] += 1

        seen_with_sum = defaultdict(int)
        count_map = defaultdict(int)

        # right to left
        for indx in range(size - 1, -1, -1):
            # (j1 + j2) - 2*i
            result[indx] += seen_with_sum[nums[indx]] - (count_map[nums[indx]] * indx)
            seen_with_sum[nums[indx]] += indx
            count_map[nums[indx]] += 1

        return result
        # v1 my solution
        # ans = []
        # for indx_i, item_i in enumerate(nums):
        #     tmp = 0
        #     for indx_j, item_j in enumerate(nums):
        #         if item_i == item_j and indx_i != indx_j:
        #             tmp += abs(indx_i - indx_j)
        #     ans.append(tmp)
        # return ans
