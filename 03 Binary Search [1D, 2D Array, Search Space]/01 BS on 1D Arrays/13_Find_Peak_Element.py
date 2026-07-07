# Given an array arr of integers. A peak element is defined as an element greater than both of its neighbors.

# Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i].

# Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.

# Note:

# As there can be many peak values, "true" is given as output if the returned index is a peak number, otherwise the returned value of index.

# Example 1
# Input : arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
# Output: 7
# Explanation: In this example, there is only 1 peak that is at index 7.

# Example 2
# Input : arr = [1, 2, 1, 3, 5, 6, 4]
# Output: 1
# Explanation: In this example, there are 2 peak numbers at indices 1 and 5. We can consider any of them.





# Time Complexity: O(n) - We are iterating through the entire array to find the peak element.
# Space Complexity: O(1) - We are not using any extra space.
from git import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range (n):
            left = (i == 0) or (nums[i] >= nums[i-1])
            right = (i == n - 1) or (nums[i] >= nums[i+1])
            if left and right:
                return i
        return -1
    


# Time Complexity: O(log n) - We are using binary search to find the peak element.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low