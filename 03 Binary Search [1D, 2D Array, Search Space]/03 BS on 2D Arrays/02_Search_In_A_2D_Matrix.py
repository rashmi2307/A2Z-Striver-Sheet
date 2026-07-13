# Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, and the first element of a row is greater than the last element of the previous row (if it exists), and an integer target, determine if the target exists in the given mat or not.

# Example 1
# Input: mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], target = 8
# Output: True
# Explanation: The target = 8 exists in the 'mat' at index (1, 3).

# Example 2
# Input: mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ], target = 78
# Output: False
# Explanation: The target = 78 does not exist in the 'mat'. Therefore in the output, we see 'false'.




# Brute Force Approach:
# Time Complexity: O(m*n) - We are traversing the entire matrix to find the target.
# Space Complexity: O(1) - We are not using any extra space.
from git import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        for i in range (m):
            for j in range (len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False
                



# Better Approach:
# Time Complexity: O(m+n) - We are traversing the matrix in a linear fashion to find the target element.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        for i in range (n):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                return self.binarySearch(matrix[i], target)

        return False
                
    def binarySearch(self, matrix, target):
        low = 0
        high = len(matrix)-1
        while low <= high:
            mid = (low+high)//2

            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                low = mid+1
            else:
                high = mid - 1
        return False
    





# Optimal Approach:
# Time Complexity: O(log(m*n)) - We are performing binary search on the entire matrix
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n * m - 1

        while low <= high:
            mid = (low+high)//2

            row = mid // m
            column = mid % m

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False