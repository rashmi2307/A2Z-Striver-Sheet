# Given an array of integers called nums, sort the array in non-decreasing order using the quick sort algorithm and return the sorted array.

# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.

# Example 1 Input: nums = [7, 4, 1, 5, 3] Output: [1, 3, 4, 5, 7]

# Explanation: 1 <= 3 <= 4 <= 5 <= 7. Thus the array is sorted in non-decreasing order.

# Example 2 Input: nums = [5, 4, 4, 1, 1] Output: [1, 1, 4, 4, 5]

# Explanation: 1 <= 1 <= 4 <= 4 <= 5. Thus the array is sorted in non-decreasing order.



class Solution:
    def quickSort(self, nums):
        self.sort(nums, 0, len(nums)-1)
        return nums

    def sort(self, nums, low, high):
        if low < high:
            partition_index = self.function(nums, low, high)
            self.sort(nums, low, partition_index-1)
            self.sort(nums, partition_index+1, high)

    def function(self, nums, low, high):
        pivot = nums[low]
        i = low
        j = high
        while i<j:
            while i<=high-1 and nums[i]<=pivot:
                i+=1
            while j>=low and nums[j]>pivot:
                j-=1
            if i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        nums[j], nums[low] = nums[low], nums[j]
        return j
            