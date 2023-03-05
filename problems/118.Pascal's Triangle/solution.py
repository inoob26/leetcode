from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = 1
        result = []
        while row <= numRows:
            if row < 3:
                newarr = [1] * row
            else:
                newarr = [1]
                for i in range(len(result[row - 2]) - 1):
                    element = result[row - 2][i] + result[row - 2][i + 1]
                    newarr.append(element)
                newarr.append(1)

            result.append(newarr)
            row += 1
        return result
