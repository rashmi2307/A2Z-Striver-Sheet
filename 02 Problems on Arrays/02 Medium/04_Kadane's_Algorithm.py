# Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1
# Input: nums = [2, 3, 5, -2, 7, -4]
# Output: 15
# Explanation:
# The subarray from index 0 to index 4 has the largest sum = 15

# Example 2
# Input: nums = [-2, -3, -7, -2, -10, -4]
# Output: -2
# Explanation:
# The element on index 0 or index 3 make up the largest sum when taken as a subarray


# Brute Force Approach
# Time Complexity: O(n^3) where n is the length of the input array  
# Space Complexity: O(1) as we are using only constant space to store the maximum sum
from typing import List
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        maxi = float("-inf")
        for i in range (n):
            for j in range (n):
                sumz = 0
                for k in range (i, j+1):
                    sumz += nums[k]
                    maxi = max(sumz, maxi)
        return maxi
    


# Better Approach
# Time Complexity: O(n^2) where n is the length of the input array  
# Space Complexity: O(1) as we are using only constant space to store the maximum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float("-inf")
        for i in range (n) :
            sum = 0
            for j in range (i, n):
                sum += nums[j]
                maxi = max(sum, maxi)
        return maxi
    



# Optimal Approach : Kadane's Algorithm
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the maximum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        sum = 0
        for i in range (len(nums)) :
            sum += nums[i]
            if sum > maxi:
                maxi = sum
            if sum <0:
                sum = 0
        return maxi