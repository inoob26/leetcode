class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        start = ord("A")
        result = 0

        for char in columnTitle:
            result = result * 26
            result += ord(char) - start + 1
        return result
