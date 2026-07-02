# Given an integer array nums. Return the number of reverse pairs in the array.
# An index pair (i, j) is called a reverse pair if:

# 0 <= i < j < nums.length
# nums[i] > 2 * nums[j]

# Example 1
# Input: nums = [6, 4, 1, 2, 7]
# Output: 3
# Explanation:
# The reverse pairs are:
# (0, 2) : nums[0] = 6, nums[2] = 1, 6 > 2 * 1
# (0, 3) : nums[0] = 6, nums[3] = 2, 6 > 2 * 2
# (1, 2) : nums[1] = 4, nums[2] = 1, 4 > 2 * 1

# Example 2
# Input: nums = [5, 4, 4, 3, 3]
# Output: 0
# Explanation:
# No pairs satisfy both the conditons.




# Brute Force Approach: Time Limit exceeded for large inputs. We can optimize this using merge sort technique.
# Time Complexity: O(n^2) where n is the length of the input array
from ast import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range (n):
            for j in range (i+1,n):
                if nums[i] > 2* nums[j]:
                    count += 1
        return count
    



