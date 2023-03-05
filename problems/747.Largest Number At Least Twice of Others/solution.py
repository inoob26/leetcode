from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        s = sorted(nums)
        tmp = 2 * s[-2]
        if s[-1] >= tmp:
            return nums.index(s[-1])
        else:
            return -1
