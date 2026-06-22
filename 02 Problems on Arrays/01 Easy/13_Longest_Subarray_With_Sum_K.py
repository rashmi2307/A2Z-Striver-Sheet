# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

# Example 1
# Input: nums = [10, 5, 2, 7, 1, 9],  k=15
# Output: 4
# Explanation:
# The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

# Example 2
# Input: nums = [-3, 2, 1], k=6
# Output: 0
# Explanation:
# There is no sub-array in the array that sums to 6. Therefore, the output is 0.



# Brute Force Solution
# Time Complexity: O(n^3) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the sum
class Solution:
    def longestSubarray(self, nums, k):
        length = 0
        n = len(nums)
        for i in range (n):
            for j in range(i,n):
                sumz = 0
                for l in range(i,j+1):
                    sumz = sumz+nums[l]
                if sumz == k:
                    length = max(length, j-i+1)
        return length
    


# Better Solution
# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the sum
class Solution:
    def longestSubarray(self, nums, k):
        length = 0
        n = len(nums)
        for i in range (n):
            sumz = 0
            for j in range(i,n):
                sumz = sumz+nums[j]
                if sumz == k:
                    length = max(length, j-i+1)
        return length
    

# Optimal Solution
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) as we are using a dictionary to store the sum and its index


# 1. Add current element to running sum.

# 2. If currentSum == k:
#       subarray from 0 to current index is valid.

# 3. Compute:
#       required = currentSum - k

# 4. If required has been seen before:
#       a valid subarray exists ending here.

# 5. Calculate its length using:
#       current index - first occurrence index

# 6. Update maximum length.

# 7. Store currentSum in hashmap
#       ONLY if it has not been seen before.

class Solution:
    def longestSubarray(self, nums, k):
        sumz = 0
        length = 0
        hashmap = {}
        for i in range(len(nums)):
            sumz = sumz + nums[i]
            if sumz == k:
                length = max(length, i+1)
            required = sumz - k
            if required in hashmap:
                length = max(length, i - hashmap[required])
            if sumz not in hashmap:
                hashmap[sumz] = i
        return length

                