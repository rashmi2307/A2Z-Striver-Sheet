# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1

# Example 1
# Input: nums = [2, 3, 4, 5, 3], target = 3
# Output: 1
# Explanation:
# The first occurence of 3 in nums is at index 1

# Example 2
# Input: nums = [2, -4, 4, 0, 10], target = 6
# Output: -1
# Explanation:
# The value 6 does not occur in the array, hence output is -1



class Solution:
    def linearSearch(self, nums, target):
        i = 0
        while i < len(nums):
            if target != nums[i]:
                i+=1
            else:
                return i
        return -1