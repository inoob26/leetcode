class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        index_map = {}
        words = s.split()
        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = "char_{}".format(c)
            char_word = "word_{}".format(w)

            if char_key not in index_map:
                index_map[char_key] = i

            if char_word not in index_map:
                index_map[char_word] = i

            if index_map[char_key] != index_map[char_word]:
                return False

        return True


# my solution
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         if len(pattern) != len(s.split(" ")):
#             return False

#         match_map = {}
#         for indx, item in enumerate(s.split(" ")):
#             if pattern[indx] not in match_map.keys() and item not in match_map.values():
#                 match_map[pattern[indx]] = item
#             elif (pattern[indx], item) not in match_map.items() or match_map[
#                 pattern[indx]
#             ] != item:
#                 return False

#         return True
