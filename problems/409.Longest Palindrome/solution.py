from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        len, has_odd = 0, 0
        for char_val in Counter(s).values():
            if char_val % 2:
                has_odd = 1
                len += char_val - 1
            else:
                len += char_val

        return len + 1 * has_odd
