from typing import List


# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         line1 = set("qwertyuiop")
#         line2 = set("asdfghjkl")
#         line3 = set("zxcvbnm")

#         return [
#             word
#             for word in words
#             if set(word.lower()).issubset(line1)
#             or set(word.lower()).issubset(line3)
#             or set(word.lower()).issubset(line2)
#         ]


# my solution
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        result = []

        for word in words:
            chars = [char.lower() for char in word]
            w_in_first = all(char in first_row for char in chars)
            w_in_second = all(char in second_row for char in chars)
            w_in_third = all(char in third_row for char in chars)
            if any((w_in_first, w_in_second, w_in_third)):
                result.append(word)

        return result
