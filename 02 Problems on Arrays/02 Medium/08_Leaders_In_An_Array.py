# Given an integer array nums, return a list of all the leaders in the array.

# A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.

# Example 1
# Input: nums = [1, 2, 5, 3, 1, 2]
# Output: [5, 3, 2]
# Explanation:
# 2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]

# Example 2
# Input: nums = [-3, 4, 5, 1, -4, -5]
# Output: [5, 1, -4, -5]
# Explanation:
# -5 is the rightmost element, -4 is the largest element in the index range [4, 5], 1 is the largest element in the index range [3, 5] and 5 is the largest element in the range [2, 5]



# Brute Force Approach
# Time Complexity: O(n*n) where n is the length of the input array
# Space Complexity: O(n) as we are storing all the leaders in the input array
class Solution:
    def leaders(self, nums):
        n = len(nums)
        temp = []
        for i in range (n):
            leader = True
            for j in range (i+1,n):
                if nums[j] >= nums[i]:
                    leader = False
                    break
            if leader:
                temp.append(nums[i])
        return temp
    


# Optimal Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) as we are storing all the leaders in the input array
class Solution:
    def leaders(self, nums):
        n = len(nums)
        ans = []
        ans.append(nums[n-1])
        maxi = nums[n-1]
        for i in range (n-2, 0, -1):
            if nums[i] > maxi:
                maxi = nums[i]
                ans.append(nums[i])
        return ans[::-1]
