# my solution
class Solution:
    # time complexity O(n)
    # space complexity O(n)
    def isPalindrome(self, s: str) -> bool:
        tmp = "".join(item for item in s.lower() if item.isalnum())
        reverse_tmp = tmp[::-1]
        return tmp == reverse_tmp


# more elegant solution
# class Solution:
# time complexity O(n)
# space complexity O(1)
#     def isPalindrome(self, s: str) -> bool:
#         left, right = 0, len(s) - 1
#         while left < right:
#             while left < right and not s[left].isalnum():
#                 left += 1
#             while left < right and not s[right].isalnum():
#                 right -= 1

#             if s[left].lower() != s[right].lower():
#                 return False

#             left += 1
#             right -= 1

#         return True
