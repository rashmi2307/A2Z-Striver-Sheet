# Given an integer array nums of even length consisting of an equal number of positive and negative integers.Return the answer array in such a way that the given conditions are met:

# Every consecutive pair of integers have opposite signs.

# For all integers with the same sign, the order in which they were present in nums is preserved.

# The rearranged array begins with a positive integer.

# Example 1
# Input : nums = [2, 4, 5, -1, -3, -4]
# Output : [2, -1, 4, -3, 5, -4]
# Explanation:
# The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions

# Example 2
# Input : nums = [1, -1, -3, -4, 2, 3]
# Output : [1, -1, 2, -3, 3, -4]
# Explanation:
# The positive number 1, 2, 3 maintain their relative positions and -1, -3, -4 maintain their relative positions


# Brute Force Approach
# Time Complexity: O(n) where n is the length of the input array    
# Space Complexity: O(n) as we are using extra space to store the positive and negative numbers
class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        pos = []
        neg = []
        for i in range(n):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        for i in range (n//2):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        return nums
    

# Optimal Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) as we are using extra space to store the result array
from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = 0
        negative = 1
        result = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                result[positive] = nums[i]
                positive += 2
            else:
                result[negative] = nums[i]
                negative += 2
        return result