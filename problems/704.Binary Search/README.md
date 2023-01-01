Leetcode problem [url](https://leetcode.com/problems/binary-search/)


Given an array of integers <em>nums</em> which is sorted in ascending order, and an integer <em>target</em>, write a function to search <em>target</em> in <em>nums</em>. If <em>target</em> exists, then return its index. Otherwise, return <em>-1</em>.

You must write an algorithm with <em>O(log n)</em> runtime complexity.


**Example 1**
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```


**Example 2**
```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```


**Constraints:**

1 <= nums.length <= 10^4

-10^4 < nums[i], target < 10^4

All the integers in nums are **unique**.

nums is sorted in ascending order.