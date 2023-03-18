class Solution:
    def calculate_nex(self, num: int) -> int:
        total_sum = 0
        while num > 0:
            num, digit = divmod(num, 10)
            total_sum += digit**2
        return total_sum

    def isHappy(self, number: int) -> bool:
        if number == 1:
            return True

        seen = set()
        while number != 1 and number not in seen:
            seen.add(number)
            number = self.calculate_nex(number)

        return number == 1
