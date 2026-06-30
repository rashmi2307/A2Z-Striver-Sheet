# You are given an integer array arr of size n which contains both positive and negative integers. Your task is to find the length of the longest contiguous subarray with sum equal to 0.

# Return the length of such a subarray. If no such subarray exists, return 0.

# Example 1
# Input: arr = [15, -2, 2, -8, 1, 7, 10, 23]
# Output: 5
# Explanation:
# The subarray [-2, 2, -8, 1, 7] sums up to 0 and has the maximum length among all such subarrays.

# Example 2
# Input: arr = [2, 10, 4]
# Output: 0
# Explanation:
# There is no subarray whose elements sum to 0.




# Brute Force Approach
# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the sum
class Solution:
    def maxLen(self, arr):
        maxi = 0
        n = len(arr)
        for i in range (n):
            sums = 0
            for j in range (i+1, n):
                sums += arr[j]
                if sums == 0 and j > maxi:
                    maxi = j
        return maxi
    




# Optimal Solution for Longest Subarray with Sum 0
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) as we are using a dictionary to store the sum and its index
class Solution:
    def maxLen(self, arr):
        sums = 0
        maxi = 0
        n = len(arr)
        hashmap = {}
        for i in range (n):
            sums += arr[i]
            if sums == 0:
                maxi = i+1
            elif sums!=0:
                if sums in hashmap:
                    maxi = max(maxi,i-hashmap[sums])
                else:
                    hashmap[sums] = i
        return maxi