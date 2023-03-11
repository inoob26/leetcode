from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        # v2
        p1 = p2 = k = 0

        while p1 < len(nums1) and p2 < len(nums2):
            num1, num2 = nums1[p1], nums2[p2]
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                nums1[k] = nums1[p1]
                p1 += 1
                p2 += 1
                k += 1

        return nums1[0:k]
        # v1
        # nums1_map = Counter(nums1)

        # p1 = 0
        # result = []
        # for num in nums2:
        #     if num < nums1[p1] or num not in nums1:
        #         continue

        #     while p1 <= len(nums1) - 1:
        #         if nums1[p1] == num and nums1_map[num] > 0:
        #             result.append(num)
        #             nums1_map[num] -= 1
        #             p1 += 1
        #             break

        #         p1 += 1
        #     if p1 == len(nums1):
        #         break
        # return result
