from collections import Counter
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for indx, num in enumerate(nums):
            if num not in left:
                left[num] = indx
            right[num] = indx
            count[num] = count.get(num, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for num in count:
            if count[num] == degree:
                ans = min(ans, right[num] - left[num] + 1)

        return ans

    # my solution
    # def findShortestSubArray(self, nums: List[int]) -> int:
    #     nums_map = Counter(nums)
    #     max_n = max(nums_map.values())
    #     max_nums = []
    #     for key, val in nums_map.items():
    #         if val == max_n:
    #             max_nums.append(key)

    #     res = 500001
    #     for max_num in max_nums:
    #         res = min(res, self._get_shortest_arr(nums, max_n, max_num))

    #     return res

    # def _get_shortest_arr(self, nums: List[int], max_n: int, max_num: int):
    #     counter = 0
    #     res = []
    #     append_flag = False
    #     for indx, num in enumerate(nums):
    #         if num == max_num:
    #             append_flag = True
    #             counter += 1
    #             res.append(num)
    #             if counter == max_n:
    #                 break
    #             continue
    #         if append_flag:
    #             res.append(num)
    #     return len(res)
