from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        sorted_potions = sorted(potions)
        result = []
        potions_size = len(potions)
        for spell in spells:
            left = 0
            right = potions_size
            while left < right:
                mid = (left + right) // 2
                if sorted_potions[mid] * spell < success:
                    left = mid + 1
                else:
                    right = mid
            result.append(potions_size - left)
        return result
