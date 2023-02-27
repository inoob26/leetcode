class Solution:
    vowels = set("aeiouAEIOU")

    def _reformat_word(self, word, indx):
        if word[0] not in self.vowels:
            word = word[1:] + word[0]
        end_of_word = "a" * (indx + 1)
        return word + "ma" + end_of_word

    def toGoatLatin(self, sentence: str) -> str:
        return " ".join(
            self._reformat_word(word, indx)
            for indx, word in enumerate(sentence.split())
        )


# my solution
# class Solution:
#     vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
#     postfix = "ma"
#     end_char = "a"

#     def _reformat_word(
#         self, word: str, startswith_vowel: bool, end_times: int = 1
#     ) -> str:
#         end_of_word = self.end_char * end_times
#         if startswith_vowel or len(word) == 1:
#             word += self.postfix
#             return f"{word}{end_of_word}"

#         temp = list(word)
#         new_word = f"{''.join(temp[1:])}{temp[0]}{self.postfix}{end_of_word}"
#         return new_word

#     def toGoatLatin(self, sentence: str) -> str:
#         result = []
#         counter = 1
#         for word in sentence.split():
#             if word.startswith(self.vowels):
#                 startswith_vowel = True
#             else:
#                 startswith_vowel = False
#             result.append(self._reformat_word(word, startswith_vowel, counter))
#             counter += 1

#         return " ".join(result)
