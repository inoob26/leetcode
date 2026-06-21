from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # https://youtu.be/CJ9EicV9nWc
        def helper(nums: List[int], level: int, currentXOR: int):
            if level == len(nums):
                return currentXOR

            include = helper(nums, level + 1, currentXOR ^ nums[level])
            exclude = helper(nums, level + 1, currentXOR)

            return include + exclude

        return helper(nums, 0, 0)

        # bits = 0
        # for n in nums:
        #     bits |= n
        # return bits * 2 ** (len(nums) - 1)

        # my not working solution
        # val_map = set()
        # result = 0
        # for p1 in nums:
        #     for p2 in nums:
        #         num = p1 ^ p2
        #         # if p1 == p2 or num in val_map:
        #         if p1 == p2:
        #             continue
        #         result += num
        #         val_map.add(num)
        #     result += p1
        # end_tmp = 0
        # for indx in range(0, len(nums) - 1):
        #     end_tmp += nums[indx] ^ nums[indx + 1]

        # return result + end_tmp
