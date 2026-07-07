# Given an array nums sorted in non-decreasing order. Every number in the array except one appears twice. Find the single number in the array.

# Example 1
# Input :nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
# Output:4
# Explanation: Only the number 4 appears once in the array.

# Example 2
# Input : nums = [1, 1, 3, 5, 5]
# Output:3
# Explanation: Only the number 3 appears once in the array.




# Time Complexity: O(n) - We are iterating through the entire array to find the single element.
# Space Complexity: O(1) - We are not using any extra space.
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        start = 0
        end = n - 1
        for i in range (n):
            if i == 0 and nums[i] != nums[i+1]:
                return nums[i]
            if i == n-1 and nums[i] != nums[i-1]:
                return nums[i]
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
        return -1
    



# Time Complexity: O(n) - We are iterating through the entire array to find the single element.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range (n):
            answer ^= nums[i]
        return answer
    




# Time Complexity: O(log n) - We are using binary search to find the single element.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        low = 1
        high = n - 2

        while low <= high:

            mid = (low+high)//2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]

            if (mid%2 == 1 and nums[mid] == nums[mid-1]) or (mid%2 == 0 and nums[mid] == nums[mid+1]):
                low = mid + 1
            else:
                high = mid - 1

        return -1