from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        prev_sum = 0
        for indx, item in enumerate(nums):
            if indx == 0:
                prev_sum = item
                result.append(item)
                continue
            prev_sum += item
            result.append(prev_sum)

        return result
