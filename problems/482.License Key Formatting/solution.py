class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count = 0
        result_str = [""]
        for i in reversed(range(len(s))):
            if s[i] == "-":
                continue

            result_str.append(s[i].upper())
            count += 1
            if count == k:
                count = 0
                result_str.append("-")

        if len(result_str) > 0 and result_str[len(result_str) - 1] == "-":
            result_str = result_str[:-1]

        return "".join(result_str[::-1])
