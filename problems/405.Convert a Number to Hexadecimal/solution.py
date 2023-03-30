class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        num_map = "0123456789abcdef"

        if num < 0:
            num = (1 << 32) + num

        transition_num = num
        result = ""
        while transition_num != 0:
            reminder = transition_num % 16
            result = num_map[reminder] + result
            transition_num //= 16

        return result
