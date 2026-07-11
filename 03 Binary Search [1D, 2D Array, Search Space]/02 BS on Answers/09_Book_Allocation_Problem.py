# Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, and an integer m representing the number of students, allocate all the books to the students so that each student gets at least one book, each book is allocated to only one student, and the allocation is contiguous.

# Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized. If the allocation of books is not possible, return -1.

# Example 1
# Input: nums = [12, 34, 67, 90], m=2
# Output: 113
# Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

# Example 2
# Input: nums = [25, 46, 28, 49, 24], m=4
# Output: 71
# Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.



# Brute Force Approach:
# Time Complexity: O(n^2) - We are iterating through the entire array and for each element, we are iterating through the entire array again to count the number of students required.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def findPages(self, nums, m):
        n = len(nums)
        if m > n:
            return -1
        
        low = max(nums)
        high = sum(nums)

        for pages in range (low, high+1):
            if self.countStudents(nums, pages) == m:
                return pages
        return low

    def countStudents(self, nums, pages):
        n = len(nums)
        student = 1
        pagesStudent = 0
        for i in range (n):
            if pagesStudent + nums[i] <= pages:
                pagesStudent += nums[i]
            else:
                student += 1
                pagesStudent = nums[i]
        return student
    



# Optimized Approach:
# Time Complexity: O(n log n) - We are using binary search to find the minimum number of pages that can be allocated to a student.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def findPages(self, nums, m):
        n = len(nums)
        if m > n:
            return -1
        
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = low + (high - low)//2 
            students = self.countStudents(nums, mid)
            if students > m:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def countStudents(self, nums, pages):
        n = len(nums)
        student = 1
        pagesStudent = 0
        for i in range (n):
            if pagesStudent + nums[i] <= pages:
                pagesStudent += nums[i]
            else:
                student += 1
                pagesStudent = nums[i]
        return student
