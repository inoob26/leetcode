from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        cols = len(words[0])
        char_map = [[0 for _ in range(26)] for _ in range(cols)]

        MOD = 10**9 + 7

        def gen_ways(indx: int, t_indx: int):
            if t_indx == len(target):
                return 1

            if indx == cols:
                return 0

            res = 0
            res += gen_ways(indx + 1, t_indx)

            char = target[t_indx]
            res += gen_ways(indx + 1, t_indx + 1) * char_map[indx][ord(char) - ord("a")]

            return res % MOD

        for word in words:
            for indx, char in enumerate(word):
                char_map[indx][ord(char) - ord("a")] += 1

        return gen_ways(0, 0) % MOD
