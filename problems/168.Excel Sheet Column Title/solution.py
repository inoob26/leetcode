class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        start = ord("A")
        title = ""
        while columnNumber > 0:
            columnNumber -= 1
            title = chr(columnNumber % 26 + start) + title
            columnNumber //= 26
        return title
