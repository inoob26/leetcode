from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        is_prime_size = max([max(row) for row in nums])
        is_prime = [True for _ in range(is_prime_size + 1)]
        # 0 and 1 is not prime
        is_prime[0] = is_prime[1] = False

        for num in range(2, is_prime_size + 1):
            if not is_prime[num]:
                continue

            for indx_j in range(num**2, is_prime_size + 1, num):
                is_prime[indx_j] = False

        result = 0
        rows = len(nums)
        for row in range(rows):
            if is_prime[nums[row][row]]:
                result = max(result, nums[row][row])
            if is_prime[nums[row][rows - row - 1]]:
                result = max(result, nums[row][rows - row - 1])
        return result
