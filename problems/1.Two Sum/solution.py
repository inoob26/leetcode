from typing import List

# NOT MY SOLUTION =(
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, item in enumerate(nums):
            comp = target - nums[index]
            if comp in hashmap:
                return [index, hashmap[comp]]
            hashmap[nums[index]] = index


# my not idial code with bugs =(((((
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         temp_indexes: List[int] = []
#         result: List[int] = []
#         for index, item in enumerate(nums):
#             if item > target:
#                 continue

#             temp_indexes.append(index)

#         counter = 0
#         while counter < len(temp_indexes) - 1:
#             temp_sum = int(nums[temp_indexes[counter]]) + int(
#                 nums[temp_indexes[counter + 1]]
#             )

#             if temp_sum == target:
#                 result.append(temp_indexes[counter])
#                 result.append(temp_indexes[counter + 1])
#                 break
#             counter += 1

#         return result
