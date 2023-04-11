from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def check_pairs(num: int) -> bool:
            seen = set()
            pairs = 0
            for indx in range(1, len(nums)):
                is_not_seen = indx not in seen and indx - 1 not in seen
                if nums[indx] - nums[indx - 1] <= num and is_not_seen:
                    seen.add(indx)
                    seen.add(indx - 1)
                    pairs += 1
                    if pairs >= p:
                        return True
            return False

        nums.sort()
        left = -1
        right = 10**9 + 1
        while right - left > 1:
            mid = (left + right) >> 1
            if check_pairs(mid):
                right = mid
            else:
                left = mid
        return right
