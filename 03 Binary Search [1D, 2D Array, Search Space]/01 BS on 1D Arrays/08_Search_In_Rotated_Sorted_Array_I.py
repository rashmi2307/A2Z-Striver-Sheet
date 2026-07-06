# Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

# Example 1
# Input : nums = [4, 5, 6, 7, 0, 1, 2], k = 0
# Output: 4
# Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

# Example 2
# Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3
# Output: -1
# Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.




# Brute Force Approach:
# Time Complexity: O(n) - We are iterating through the entire array to find the target integer.
# Space Complexity: O(1) - We are not using any extra space.

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range (n):
            if target == nums[i]:
                return i
        return -1
    


# Binary Search Approach:
# Time Complexity: O(log n) - We are iterating through the entire array to find the target integer.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low+high)//2

            if target == nums[mid]:
                return mid

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
        return -1