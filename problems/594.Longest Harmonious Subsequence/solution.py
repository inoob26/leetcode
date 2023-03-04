from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counted_values = Counter(nums)
        counter = 0

        if len(counted_values.keys()) < 2:
            return 0

        for key in counted_values.keys():
            if counted_values[key + 1]:
                counter = max(counter, counted_values[key] + counted_values[key + 1])

        return counter
