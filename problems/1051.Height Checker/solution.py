from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        if expected == heights:
            return 0

        result = 0
        for indx, num in enumerate(heights):
            if num != expected[indx]:
                result += 1

        return result
