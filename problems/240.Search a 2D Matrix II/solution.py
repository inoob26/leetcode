from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time complexity : O(n+m)\mathcal{O}(n+m)O(n+m)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        colls = len(matrix[0])
        row = len(matrix) - 1
        col = 0

        while col < colls and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True

        return False

        # v1 my solution
        # def find_target_in_row(nums: List[int], target: int) -> bool:
        #     left = 0
        #     right = len(nums) - 1

        #     while left <= right:
        #         mid = (left + right) // 2
        #         if nums[mid] == target:
        #             return True
        #         elif nums[mid] < target:
        #             left = mid + 1
        #         else:
        #             right = mid - 1

        #     return False

        # for row in matrix:
        #     if find_target_in_row(row, target):
        #         return True

        # return False
