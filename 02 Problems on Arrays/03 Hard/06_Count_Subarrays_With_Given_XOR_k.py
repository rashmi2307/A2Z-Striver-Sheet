# Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.

# Example 1
# Input : nums = [4, 2, 2, 6, 4], k = 6
# Output : 4
# Explanation : The subarrays having XOR of their elements as 6 are [4, 2],  [4, 2, 2, 6, 4], [2, 2, 6], and [6]

# Example 2
# Input :nums = [5, 6, 7, 8, 9], k = 5
# Output : 2
# Explanation : The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]




# Brute Force Approach
# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the xor
class Solution:
    def subarraysWithXorK(self, nums, k):
        n = len(nums)
        counter = 0
        for i in range (n):
            xor = 0
            for j in range (i,n):
                xor ^= nums[j]
                if xor == k:
                    counter += 1
        return counter
    


# Optimal Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) as we are using a dictionary to store the xor and its
class Solution:
    def subarraysWithXorK(self, nums, k):
        freq = {0:1}
        n = len(nums)
        prefixXor = 0
        count = 0
        for num in nums:
            prefixXor ^= num
            target = prefixXor ^ k
            if target in freq:
                count += freq[target]
            freq[prefixXor] = freq.get(prefixXor,0) + 1
        return count