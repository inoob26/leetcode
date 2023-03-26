from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # leetcode answer
        p1 = curr = 0
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p1] = nums[p1], nums[curr]
                curr += 1
                p1 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

        # v2 my solution insert sort
        # for p1 in range(1, len(nums)):
        #     item = nums[p1]
        #     p2 = p1 - 1
        #     while p2 >= 0 and item < nums[p2]:
        #         nums[p2 + 1] = nums[p2]
        #         p2 -= 1
        #     nums[p2 + 1] = item

        # v1 my solution with bug
        # p1 = 0
        # p2 = len(nums) - 1

        # def swap_items(p1: int, p2: int):
        #     tmp = nums[p1]
        #     nums[p1] = nums[p2]
        #     nums[p2] = tmp

        # while p1 < p2:
        #     if nums[p1] > nums[p2]:
        #         swap_items(p1, p2)
        #         p1 += 1
        #     elif nums[p1] < nums[p2]:
        #         p1 += 1
        #     elif nums[p1] == nums[p2]:
        #         p2 -= 1
