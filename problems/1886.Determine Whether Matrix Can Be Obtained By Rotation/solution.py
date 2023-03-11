from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        # v2
        repeat = 3
        for _ in range(3):
            mat = [list(row[::-1]) for row in zip(*mat)]
            if mat == target:
                return True
        return False

        # v1
        # repeat = 3
        # tmp = []
        # for _ in range(repeat):
        #     for row in zip(*mat):
        #         tmp.append([i for i in row[::-1]])

        #     if tmp == target:
        #         return True
        #     mat = tmp
        #     tmp = []

        # return False
