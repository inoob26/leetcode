class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        is_negative = num < 0
        transition_num = num if not is_negative else -num
        result = ""
        while transition_num != 0:
            reminder = str(transition_num % 7)
            result = reminder + result
            transition_num //= 7
        if is_negative:
            result = "-" + result
        return result
