# Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order, find the index of the row with the maximum number of ones.

# If two rows have the same number of ones, consider the one with a smaller index. If no 1 exists in the matrix, return -1.

# Example 1
# Input : mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]
# Output: 0
# Explanation: The row with the maximum number of ones is 0 (0 - indexed).

# Example 2
# Input: mat = [ [0, 0], [0, 0] ]
# Output: -1
# Explanation: The matrix does not contain any 1. So, -1 is the answer.




# Brute Force Approach:
# Time Complexity: O(m*n) - We are traversing the entire matrix to count the number of 1s in each row.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def rowWithMax1s(self, mat):
        max_count = 0
        index = -1
        for i in range (len(mat)):
            count = 0
            for j in range (len(mat[i])):
                count += mat[i][j]
            if count > max_count:
                max_count = count
                index = i
        return index
    


# Optimized Approach:
# Time Complexity: O(m*log(n)) - We are performing binary search on each row    

class Solution:
    def rowWithMax1s(self, mat):
        n = len(mat)
        max_count = 0
        index = -1
        for i in range (n):
            count = self.lower_bound(mat, n, 1)
            if count > max_count:
                max_count = count
                index = i
        return index
    
    def lower_bound(self, mat, n , x):
        low, high = 0, n-1
        answer = n

        while low <= high:
            mid = (low+high)//2
            if mat[mid] >= x:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer