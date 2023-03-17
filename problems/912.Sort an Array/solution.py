from typing import List
from collections import Counter


# v1 merge sort
def merge_sort(arr: List[int]) -> None:
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_arrays(arr1=left, arr2=right, arr=arr)


def merge_two_arrays(arr1: List[int], arr2: List[int], arr: List[int]) -> None:
    size_arr1 = len(arr1)
    size_arr2 = len(arr2)
    p1 = p2 = indx = 0

    while p1 < size_arr1 and p2 < size_arr2:
        if arr1[p1] <= arr2[p2]:
            arr[indx] = arr1[p1]
            p1 += 1
        else:
            arr[indx] = arr2[p2]
            p2 += 1
        indx += 1

    while p1 < size_arr1:
        arr[indx] = arr1[p1]
        p1 += 1
        indx += 1

    while p2 < size_arr2:
        arr[indx] = arr2[p2]
        p2 += 1
        indx += 1


# v2 Counting sort
def counting_sort(arr):
    min_val = min(arr)  # O(n)
    max_val = max(arr) + 1  # O(n)

    val_map = Counter(arr)  # O(n)
    indx = 0
    for val in range(min_val, max_val):  # O(n)
        if val_map[val]:
            while val_map[val] > 0:
                arr[indx] = val
                indx += 1
                val_map[val] -= 1


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge_sort(nums)
        counting_sort(nums)
        return nums
