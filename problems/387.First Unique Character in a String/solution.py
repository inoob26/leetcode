from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {key: val for key, val in Counter(s).items() if val == 1}
        for indx, char in enumerate(s):
            if char in char_map:
                return indx

        return -1
