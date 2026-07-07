# Given an integer array nums of size N, sorted in ascending order with distinct values, and then rotated an unknown number of times (between 1 and N), find the minimum element in the array.

# Example 1
# Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]
# Output: 0
# Explanation: Here, the element 0 is the minimum element in the array.

# Example 2
# Input : nums = [3, 4, 5, 1, 2]
# Output: 1
# Explanation:Here, the element 1 is the minimum element in the array.




# Brute Force Approach:
# Time Complexity: O(n) - We are iterating through the entire array to find the minimum element.
# Space Complexity: O(1) - We are not using any extra space.    
from git import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float("inf")
        for i in range (n):
            if nums[i] < mini:
                mini = nums[i]
        return mini
    




# Binary Search Approach:
# Time Complexity: O(log n) - We are using binary search to find the minimum element
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        while start < end:

            mid = start + (end - start)//2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid 

        return nums[start]