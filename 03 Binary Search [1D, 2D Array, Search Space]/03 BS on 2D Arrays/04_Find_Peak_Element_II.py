# Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the array [i, j].A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbours to the left, right, top, and bottom.
# Assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
# Note: As there can be many peak values, 1 is given as output if the returned index is a peak number, otherwise 0.

# Example 1
# Input: mat=[[10, 20, 15], [21, 30, 14], [7, 16, 32]]
# Output: [1, 1]
# Explanation: The value at index [1, 1] is 30, which is a peak element because all its neighbours are smaller or equal to it. Similarly, {2, 2} can also be picked as a peak.

# Example 2
# Input: mat=[[10, 7], [11, 17]]
# Output : [1, 1]
# Explanation:The value at index [1, 1] is 17, which is the only peak element because all its neighbours are smaller or equal to it.





from git import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        low, high = 0, n-1
        while low <= high:
            mid = (low+high)//2
            row = self.row_search(mat, mid)

            left = mat[row][mid-1] if mid-1 >= 0 else float('-inf')
            right = mat[row][mid+1] if mid+1 < n else float('-inf')

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row,mid]
            elif left > mat[row][mid]:
                high = mid - 1
            else:
                low = mid + 1

        return [-1,-1]
    
    def row_search(self, mat, col):
        index = -1
        max_val = float('-inf')

        for i in range (len(mat)):
            if mat[i][col] > max_val:
                max_val = mat[i][col]
                index = i
        return index