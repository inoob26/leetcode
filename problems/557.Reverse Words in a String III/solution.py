class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for word in s.split():
            result.append("".join(list(word)[::-1]))

        return " ".join(result)


# first version
# class Solution:
#     @staticmethod
#     def helper(s: List[str]) -> str:
#         l = 0
#         r = len(s) - 1

#         while l < r:
#             temp = s[l]
#             s[l] = s[r]
#             s[r] = temp
#             l += 1
#             r -= 1

#         return ''.join(s)

#     def reverseWords(self, s: str) -> str:
#         result = []

#         for item in s.split():
#             result.append(self.helper(list(item)))

#         return ' '.join(result)
