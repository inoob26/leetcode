class Solution:
    def partitionString(self, s: str) -> int:
        # v3 optimize my solution
        result = 1
        substr = ""
        for char in s:
            if char not in substr:
                substr += char
            else:
                substr = char
                result += 1
        return result

        # v2 leetcode solution
        # seen = [-1] * 26
        # result = 1
        # substringStarting = 0

        # for indx in range(len(s)):
        #     if seen[ord(s[indx]) - ord("a")] >= substringStarting:
        #         substringStarting = indx
        #         result += 1
        #     seen[ord(s[indx]) - ord("a")] = indx

        # return result

        # v1 my solution
        # result = 0
        # substr = ""
        # for indx, char in enumerate(s):
        #     if char not in substr:
        #         substr += char

        #     if indx + 1 <= len(s) - 1 and s[indx + 1] in substr:
        #         result += 1
        #         substr = ""
        # if substr:
        #     result += 1
        # return result
