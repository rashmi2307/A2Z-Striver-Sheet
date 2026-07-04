# Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.

# Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.

# Note: You are not allowed to modify the original array.

# Example 1
# Input: nums = [3, 5, 4, 1, 1]
# Output: [1, 2]
# Explanation:
# 1 appears two times in the array and 2 is missing from nums

# Example 2
# Input: nums = [1, 2, 3, 6, 7, 5, 7]
# Output: [7, 4]
# Explanation:
# 7 appears two times in the array and 4 is missing from nums.


# Brute Force Approach:
# Time Complexity: O(n^2) - We are using the count() function inside a loop, which results in a nested loop behavior.
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        repeating,missing = -1,-1
        for i in range (1,n+1):
            count = nums.count(i)

            if count == 2:
                repeating = i
            elif count == 0:
                missing = i

            if repeating != -1 and missing != -1:
                break

        return [repeating, missing]
    



# Better Approach:
# Time Complexity: O(n) - We are using a single loop to iterate through the array
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        hashmap = [0]*(n+1)

        for num in nums:
            hashmap[num] += 1
        repeating, missing = -1, -1

        for i in range (1,n+1):
            if hashmap[i] == 2:
                repeating = i 
            elif hashmap[i] == 0:
                missing = i 

            if repeating != -1 and missing != -1:
                break

        return [repeating, missing]