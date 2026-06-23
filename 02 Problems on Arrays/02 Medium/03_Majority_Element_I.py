# Given an integer array nums of size n, return the majority element of the array.

# The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

# Example 1
# Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
# Output: 7
# Explanation:
# The number 7 appears 5 times in the 9 sized array

# Example 2
# Input: nums = [1, 1, 1, 2, 1, 2]
# Output: 1
# Explanation:
# The number 1 appears 4 times in the 6 sized array



# Moore's Voting Algorithm
# Time Complexity: O(n) where n is the length of the input array    
# Space Complexity: O(1) as we are using only constant space to store the count and candidate
class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        count = 0
        for i in range (n):
            if count == 0:
                candidate = nums[i]
                count = 1
            else:
                if nums[i] == candidate:
                    count+=1
                else:
                    count -= 1
        return candidate