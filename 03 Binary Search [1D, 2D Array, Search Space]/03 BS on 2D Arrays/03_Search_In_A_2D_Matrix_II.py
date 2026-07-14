# Given a 2D array matrix where each row is sorted in ascending order from left to right and each column is sorted in ascending order from top to bottom, write an efficient algorithm to search for a specific integer target in the matrix.

# Example 1
# Input: matrix = [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ], target = 5
# Output: True
# Explanation: The target 5 exists in the matrix in the index (1,1)

# Example 2
# Input: matrix= [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ], target = 20
# Output: False
# Explanation: The target 20 does not exist in the matrix.





# Brute Force Approach:
# Time Complexity: O(m*n) - We are traversing the entire matrix to find the target element.
# Space Complexity: O(1) - We are not using any extra space.
from ast import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range (m):
            for j in range (n):
                if matrix[i][j] == target:
                    return True
        return False






# Better Approach:
# Time Complexity: O(m+n) - We are traversing the matrix in a linear fashion to find the target element.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:

    def binary_search(self, nums, target) -> bool:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2 
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for row in matrix:
            found_in_row = self.binary_search(row, target)
            if found_in_row:
                return True
        return False 






# Optimal Approach:
# Time Complexity: O(m+n) - We are traversing the matrix in a linear fashion
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        row = 0
        col = m-1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False