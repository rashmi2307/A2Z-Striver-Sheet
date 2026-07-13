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
                


# Optimized Approach:
# Time Complexity: O(log(m*n)) - We are performing binary search on the entire matrix   
