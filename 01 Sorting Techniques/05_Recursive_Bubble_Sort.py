# Given an array of integers nums, sort the array in non-decreasing order using the recursive Bubble Sort algorithm, and return the sorted array.

# You must implement Bubble Sort using recursion only. Do not use built-in sorting functions (sort, sorted, Arrays.sort, etc.). A sorted array in non-decreasing order is an array where each element is greater than or equal to the previous one.

# Example 1 Input: nums = [7, 4, 1, 5, 3] Output: [1, 3, 4, 5, 7]

# Explanation: 1 <= 3 <= 4 <= 5 <= 7. Thus the array is sorted in non-decreasing order.

# Example 2 Input: nums = [5, 4, 4, 1, 1] Output: [1, 1, 4, 4, 5]

# Explanation: 1 <= 1 <= 4 <= 4 <= 5. Thus the array is sorted in non-decreasing order.



class Solution:
    def bubbleSort(self, nums):
        self.sort(nums,len(nums))
        return nums

    def sort(self,nums,n):
        swapped = False
        if n == 1:
            return
        for j in range (n-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if swapped == False:
            return 
        self.sort(nums,n-1)