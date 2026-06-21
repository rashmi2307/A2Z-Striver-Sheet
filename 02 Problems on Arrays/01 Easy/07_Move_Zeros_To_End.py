# Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same.

# This must be done in place, without making a copy of the array.

# Example 1
# Input: nums = [0, 1, 4, 0, 5, 2]
# Output: [1, 4, 5, 2, 0, 0]
# Explanation:
# Both the zeroes are moved to the end and the order of the other elements stay the same

# Example 2
# Input: nums = [0, 0, 0, 1, 3, -2]
# Output: [1, 3, -2, 0, 0, 0]
# Explanation:
# All 3 zeroes are moved to the end and the order of the other elements stay the same


# Optimized Solution
# Time Complexity: O(n)
class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        j = 0
        while j < n:
            if nums[j] == 0:
                j+=1
            else:
                nums[i] = nums[j]
                i+=1
                j+=1
        while i < n:
            nums[i] = 0
            i+=1


# Brute Force Solution
# Time Complexity: O(n^2)
class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        temp = 0
        for i in range (n):
            if nums[i] == 0:
                temp = 0
                nums.remove(0)
                nums.append(temp)