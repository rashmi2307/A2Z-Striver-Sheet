# Given an integer array nums. Find the subarray with the largest product, and return the product of the elements present in that subarray.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1
# Input: nums = [4, 5, 3, 7, 1, 2]
# Output: 840
# Explanation:
# The largest product is given by the whole array itself

# Example 2
# Input: nums = [-5, 0, -2]
# Output: 0
# Explanation:
# The largest product is achieved with the following subarrays [0], [-5, 0], [0, -2], [-5, 0, -2].





# Brute Force Approach: Time Limit exceeded for large inputs. We can optimize this using dynamic programming technique.
# Time Complexity: O(n^2) where n is the length of the input array
from ast import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxp = float("-inf")
        for i in range (n):
            product = 1
            for j in range (i, n):
                product *= nums[j]
                if product > maxp:
                    maxp = product
        return maxp




# Optimized Approach: Using dynamic programming technique to find the maximum product subarray.
# Time Complexity: O(n) where n is the length of the input array
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix, suffix  = 1, 1
        answer = float("-inf")
        for i in range (n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix *= nums[i]
            suffix *= nums[n-i-1]
            answer = max(prefix, suffix, answer)
        return answer