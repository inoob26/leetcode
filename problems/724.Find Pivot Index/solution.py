from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for indx, item in enumerate(nums):
            left = sum(nums[:indx])
            right = sum(nums[indx:]) - item
            if left == right:
                return indx

        return -1
