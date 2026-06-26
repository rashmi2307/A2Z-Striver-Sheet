# Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.

# The rotation must be done in place, meaning the input 2D matrix must be modified directly.

# Example 1
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# Example 2
# Input: matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
# Output: matrix = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]



# Brute Force Approach
# Time Complexity: O(n^2) where n is the number of rows or columns in the input matrix
# Space Complexity: O(n^2) as we are using an extra matrix of size n
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        temp = [[0] * n for _ in range(n)]
        for i in range (n):
            for j in range (n):
                temp[j][n-i-1] = matrix[i][j]

        for i in range (n):
            for j in range (n):
                matrix[i][j] = temp[i][j] 



# Optimal Approach
# Time Complexity: O(n^2) where n is the number of rows or columns in the input matrix
# Space Complexity: O(1) as we are not using any extra space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range (n):
            for j in range (i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()