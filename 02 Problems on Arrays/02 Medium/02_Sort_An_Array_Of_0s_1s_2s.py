# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.

# The sorting must be done in-place, without making a copy of the original array.

# Example 1
# Input: nums = [1, 0, 2, 1, 0]
# Output: [0, 0, 1, 1, 2]
# Explanation:
# The nums array in sorted order has 2 zeroes, 2 ones and 1 two

# Example 2
# Input: nums = [0, 0, 1, 1, 1]
# Output: [0, 0, 1, 1, 1]
# Explanation:
# The nums array in sorted order has 2 zeroes, 3 ones and zero twos


# Brute Force Solution
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the counts
class Solution:
    def sortZeroOneTwo(self, nums):
        n = len(nums)
        count1, count2, count0 = 0, 0, 0
        for i in range (n):
            if nums[i] == 0:
                count0 += 1
            if nums[i] == 1:
                count1 += 1
            if nums[i] == 2:
                count2 += 1
        for i in range (count0):
            nums[i] = 0
        for i in range (count0, count0+count1):
            nums[i] = 1
        for i in range (count0+count1, n):
            nums[i] = 2