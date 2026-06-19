# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

# Example 1
# Input: nums = [1, 2, 3, 4, 5, 6], k = 2
# Output: nums = [3, 4, 5, 6, 1, 2]
# Explanation:
# rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
# rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]


class Solution:
    def rotateArray(self, nums, k: int) -> None:    
        n = len(nums)
        k = k % n
        for i in range ( k):
            temp = nums[0]
            for j in range (1, n):
                nums [j-1] = nums[j]
            nums[n-1] = temp
