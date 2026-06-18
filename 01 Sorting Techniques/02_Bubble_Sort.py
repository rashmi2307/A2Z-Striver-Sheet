# Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.

# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.

# Example 1 Input: nums = [7, 4, 1, 5, 3] Output: [1, 3, 4, 5, 7]

# Explanation: 1 <= 3 <= 4 <= 5 <= 7. Thus the array is sorted in non-decreasing order.

# Example 2 Input: nums = [5, 4, 4, 1, 1] Output: [1, 1, 4, 4, 5]

# Explanation: 1 <= 1 <= 4 <= 4 <= 5. Thus the array is sorted in non-decreasing order.



# Normal Complexity: O(n^2)
class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range (n-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums



# Optimized Complexity: O(n)
class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range (n-1,0,-1):
            swapped = False
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if swapped == False:
                break
        return nums
