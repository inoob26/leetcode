class Solution:
    def addDigits(self, num: int) -> int:
        # v2
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

        # v1
        # if num < 10:
        #     return num

        # number = str(num)

        # while len(number) >= 2:
        #     tmp = 0
        #     for n in number:
        #         tmp += int(n)
        #     number = str(tmp)

        # return int(number)
