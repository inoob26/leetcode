from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        positive = ""
        index = 0
        common_result_lst = []
        prefix = ""
        for c in strs[0]:
            prefix += c
            common_result_lst = list([item.startswith(prefix) for item in strs])

            if all(common_result_lst):
                positive = prefix
            else:
                break

        return positive
