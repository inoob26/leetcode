class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        ugly_nums = (2, 3, 5)

        def dividing(dividend, divisor):
            while dividend % divisor == 0:
                dividend //= divisor
            return dividend

        for i in ugly_nums:
            n = dividing(n, i)

        return n == 1
