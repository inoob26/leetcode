from collections import Counter


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_len = len(s)
        if s_len % 2 == 1:
            return False

        result = ""
        for indx, char in enumerate(s):
            if char not in result:
                result += char
                continue

            repeat_times = int(s_len / len(result))
            if result * repeat_times == s:
                return True
            else:
                result += char

        return False
