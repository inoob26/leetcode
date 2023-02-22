from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False

        return True


# my solution
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         if len(ransomNote) > len(magazine):
#             return False

#         magazine_map = Counter(magazine)
#         for c in ransomNote:
#             if c in magazine_map:
#                 magazine_map[c] -= 1
#             else:
#                 return False

#             if magazine_map[c] == -1:
#                 return False

#         return True
