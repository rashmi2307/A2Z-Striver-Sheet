# Given an integer array nums, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.

# Example 1
# Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
# Output: True
# Explanation: The element 3 is present in the array. So, the answer is True.

# Example 2
# Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
# Output: False
# Explanation:The element 10 is not present in the array. So, the answer is False.



# Brute Force Approach:
# Time Complexity: O(n) - We are iterating through the entire array to find the target integer.     
# Space Complexity: O(1) - We are not using any extra space.
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for i in range (n):
            if target == nums[i]:
                return True
        return False
    


# Binary Search Approach:
# Time Complexity: O(log n) - We are iterating through the entire array to find the target integer.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low+high)//2

            if target == nums[mid]:
                return True
            
            if nums[mid] == nums[low] == nums[high]:
                low += 1
                high -= 1
                continue

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
