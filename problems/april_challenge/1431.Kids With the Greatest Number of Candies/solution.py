from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # v2 better with
        # time: O(n)
        # space: O(1)
        greatest = max(candies)
        for indx, candies_amount in enumerate(candies):
            candies[indx] = candies_amount + extraCandies >= greatest

        return candies

        # v1 my version
        # time: O(n)
        # space: O(n)
        # greatest = max(candies)
        # result = [False for _ in range(len(candies))]

        # for indx, candies_amount in enumerate(candies):
        #     result[indx] = candies_amount + extraCandies >= greatest

        # return result
