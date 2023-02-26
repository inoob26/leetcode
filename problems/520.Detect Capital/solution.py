class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return any(
            (word.capitalize() == word, word.upper() == word, word.lower() == word)
        )
