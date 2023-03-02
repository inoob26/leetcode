from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # v2
        counter = max_count = 0
        for item in nums:
            if item == 0:
                max_count = max(max_count, counter)
                counter = 0
            else:
                counter += 1
        return max(max_count, counter)

        # v1
        # counted_lst = []
        # counter = 0
        # num_len = len(nums) - 1
        # for indx, item in enumerate(nums):
        #     if item == 0:
        #         counted_lst.append(counter)
        #         counter = 0
        #     elif item == 1:
        #         counter += 1

        #     if indx == num_len:
        #         counted_lst.append(counter)
        # return max(counted_lst)
