from typing import List


"""
Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # [2, 2, 3, 1]
        # v3
        first = float("-inf")
        second = float("-inf")
        third = float("-inf")

        for num in nums:
            if num == first or num == second or num == third:
                continue

            if first <= num:
                third = second
                second = first
                first = num
            elif second <= num:
                third = second
                second = num
            elif third <= num:
                third = num

        if third == float("-inf"):
            return first
        return third

        # v2
        # res = []
        # nums.sort(reverse=True)
        # for i in nums:
        #     if i in res:
        #         continue
        #     res.append(i)
        #     if len(res) == 3:
        #         return i

        # return res[0]

        # v1
        # result = sorted(set(nums))
        # return result[::-1][2]
