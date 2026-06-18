# Given an array of integers nums, sort the array in non-decreasing order using the recursive Insertion Sort algorithm, and return the sorted array.

# You must implement Insertion Sort using recursion only.
# Do not use loops (like for or while) or built-in sorting functions (sort, Arrays.sort, etc.).
# A sorted array in non-decreasing order is an array where each element is greater than or equal to all elements that come before it.

# Example 1
# Input: nums = [7, 4, 1, 5, 3]
# Output: [1, 3, 4, 5, 7]

# Explanation: 1 <= 3 <= 4 <= 5 <= 7.
# Thus the array is sorted in non-decreasing order.

# Example 2
# Input: nums = [5, 4, 4, 1, 1]
# Output: [1, 1, 4, 4, 5]

# Explanation: 1 <= 1 <= 4 <= 4 <= 5.
# Thus the array is sorted in non-decreasing order.



# Completely Recursive
class Solution:
    def insertionSort(self, nums):
        self.sort(nums, len(nums), 0)
        return nums

    def sort(self, nums, n, i):
        j = i
        if i == n:
            return
        self.insert(nums,j)
        self.sort(nums, n, i+1)

    def insert(self, nums, j):
        if j==0:
            return
        if nums[j-1]<=nums[j]:
            return
        nums[j-1], nums[j] = nums[j], nums[j-1]
        self.insert(nums,j-1)



class Solution:
    def insertionSort(self, nums):
        self.sort(nums, len(nums), 0)
        return nums

    def sort(self, nums, n, i):
        j = i
        if i == n:
            return
        while j>0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j-=1
        self.sort(nums, n, i+1)