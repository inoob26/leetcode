from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # v2
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            item = matrix[mid // cols][mid % cols]
            if item == target:
                return True
            else:
                if target > item:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

        # v1
        # def is_target_exists(nums: List[int], target: int) -> bool:
        #     if len(nums) == 1:
        #         return target == nums[0]

        #     l = 0
        #     r = len(nums) - 1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if nums[mid] == target:
        #             return True
        #         elif nums[mid] < target:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     return False

        # for row in matrix:
        #     last = row[-1]
        #     if target > last:
        #         continue
        #     else:
        #         return is_target_exists(row, target)
        # return False
