from typing import List


class Solution:
    def get_plus_indexes(self, digits: List[int]) -> List[int]:
        r = len(digits) - 1
        result = []
        while r != -1:
            if digits[r] == 9:
                result.append(r)
            elif digits[r] < 9:
                result.append(r)
                break
            r -= 1
        return result

    def plusOne(self, digits: List[int]) -> List[int]:
        plus_indexes = self.get_plus_indexes(digits)

        for i in plus_indexes:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1

        if all([i == 0 for i in digits]):
            return [1] + digits
        return digits
