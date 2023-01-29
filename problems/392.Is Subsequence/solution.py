class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        found_lst = []
        start_sub_point = 0
        for item in s:
            for indx_sub in range(start_sub_point, len(t)):
                if item == t[indx_sub]:
                    start_sub_point = indx_sub + 1
                    found_lst.append(t[indx_sub])
                    break

        return "".join(found_lst) == s
