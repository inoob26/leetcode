from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result: List[int] = []
        for i in range(left, right + 1, 1):
            if i % 10 == 0:
                continue
            nums = str(i)
            for num in nums:
                j = int(num)
                if j == 0 or i % j != 0:
                    break
            else:
                result.append(i)
        return result
