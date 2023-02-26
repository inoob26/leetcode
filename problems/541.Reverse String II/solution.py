class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = list(s)
        indx = k
        step = 2 * k
        for i in range(0, len(s) - 1, step):
            val = result[i:indx]
            rev_val = val[::-1]
            result[i:indx] = rev_val[0:]
            indx += step
        return "".join(result)
