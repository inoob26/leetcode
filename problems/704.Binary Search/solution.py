from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0

        left = 0
        right = len(nums) - 1
        middle = 0

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle

            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return -1
