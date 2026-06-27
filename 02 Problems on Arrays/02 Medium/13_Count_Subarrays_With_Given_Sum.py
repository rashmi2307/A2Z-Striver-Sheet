# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# Example 1
# Input: nums = [1, 1, 1], k = 2
# Output: 2
# Explanation: In the given array [1, 1, 1], there are two subarrays that sum up to 2: [1, 1] and [1, 1]. Hence, the output is 2.

# Example 2
# Input: nums = [1, 2, 3], k = 3
# Output: 2
# Explanation: In the given array [1, 2, 3], there are two subarrays that sum up to 3: [1, 2] and [3]. Hence, the output is 2.



# Brute Force Approach : Time Limit Exceeded
# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the count of subarrays
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range (n):
            sum = 0
            for j in range (i,n):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count