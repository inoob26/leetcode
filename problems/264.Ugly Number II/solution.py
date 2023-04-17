class Solution:
    def nthUglyNumber(self, n: int) -> int:
        result = [0] * n
        result[0] = 1
        p1 = p2 = p3 = 0
        for i in range(1, n):
            result[i] = min(
                result[p1] * 2,
                result[p2] * 3,
                result[p3] * 5,
            )
            if result[i] == result[p1] * 2:
                p1 += 1
            if result[i] == result[p2] * 3:
                p2 += 1
            if result[i] == result[p3] * 5:
                p3 += 1
        return result[-1]

        # v1
        # primes = (2, 3, 5)

        # def is_valid_number(num):
        #     for prime in primes:
        #         if num % prime == 0:
        #             return True
        #     return False

        # gen_num = 1
        # counter = 1
        # while counter < n:
        #     gen_num += 1
        #     while not is_valid_number(gen_num):
        #         gen_num += 1
        #     counter += 1

        # return gen_num
