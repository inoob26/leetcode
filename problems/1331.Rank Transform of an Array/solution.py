from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = 1
        rank_map = {}
        for num in sorted(arr):
            if num not in rank_map.keys():
                rank_map[num] = rank
                rank += 1

        for indx in range(len(arr)):
            arr[indx] = rank_map[arr[indx]]

        return arr
