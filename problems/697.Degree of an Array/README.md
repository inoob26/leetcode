Leetcode problem [url](https://leetcode.com/problems/degree-of-an-array/)

Given a non-empty array of non-negative integers `nums`, the **degree** of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of `nums`, that has the same degree as `nums`.


**Example 1:**
```
Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
```

**Example 2:**
```
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
```

**Constraints:**

- `nums.length` will be between 1 and 50,000.

- `nums[i]` will be an integer between 0 and 49,999.


### Simply description
It was hard for me at first but it simply that:
You search for the degree of the array by searching the most frequent element.
The subarray you try to form must have this condition:

it contains all the occurrences of the most frequent element in the original array "and all elements between those occurrences"
ex: if the original array --> arr = [1,2,2,4,2,3]
the possible subarrays are : [2,2,4,2,3] >> I removed the 1 .... or [1,2,2,4,2] >> I removed 3 ... or [2,2,4,2] >> I removed 1,3 .......
but I cannot form [2,2,2] because there is an element 4 I in-between I cannot remove it.