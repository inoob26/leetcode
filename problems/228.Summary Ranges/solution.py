from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start_range = 0
        result = []
        for indx, num in enumerate(nums):
            if indx + 1 < len(nums) and nums[indx + 1] == num + 1:
                continue

            if start_range == indx:
                result.append(str(nums[start_range]))
            else:
                result.append(f"{nums[start_range]}->{num}")

            start_range = indx + 1

        return result
