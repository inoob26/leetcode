from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        result = 0
        size = len(heights)
        for indx, num in enumerate(heights):
            while stack[-1] != -1 and num <= heights[stack[-1]]:
                # increasing monotonic stack
                curr_height = heights[stack.pop()]
                curr_widht = indx - stack[-1] - 1
                result = max(result, curr_height * curr_widht)
            stack.append(indx)

        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_widht = size - stack[-1] - 1
            result = max(result, curr_height * curr_widht)

        return result
