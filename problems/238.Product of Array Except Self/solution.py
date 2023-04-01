from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # v2
        size = len(nums)
        answer = [0] * size

        answer[0] = 1
        for indx in range(1, size):
            answer[indx] = answer[indx - 1] * nums[indx - 1]

        right = 1
        for indx in range(size - 1, -1, -1):
            answer[indx] = answer[indx] * right
            right *= nums[indx]

        return answer

        # v1
        # size = len(nums)
        # answer = [0] * size

        # left = [0] * size
        # right = [0] * size

        # left[0] = 1
        # for indx in range(1, size):
        #     left[indx] = left[indx - 1] * nums[indx - 1]

        # right[-1] = 1
        # for indx in range(size - 2, -1, -1):
        #     right[indx] = right[indx + 1] * nums[indx + 1]

        # for indx in range(len(left)):
        #     answer[indx] = left[indx] * right[indx]

        # return answer
