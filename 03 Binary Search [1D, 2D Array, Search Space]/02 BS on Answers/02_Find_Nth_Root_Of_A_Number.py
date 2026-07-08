# Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.

# Example 1
# Input: N = 3, M = 27
# Output: 3
# Explanation: The cube root of 27 is equal to 3.

# Example 2
# Input: N = 4, M = 69
# Output:-1
# Explanation: The 4th root of 69 does not exist. So, the answer is -1.




# Time Complexity: O(m) - We are iterating through the numbers from 0 to m to find the Nth root.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def NthRoot(self, n, m):
        for i in range (m):
            power = i**n
            if power == m:
                return i
            if power > m:
                break
        return -1



# Time Complexity: O(log m) - We are using binary search to find the Nth root.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def NthRoot(self, n, m):
        low, high = 1, m
        while low < high:
            mid = (low+high)//2
            power = mid**n 
            if power == m:
                return mid
            elif power < m:
                low = mid + 1
            else:
                high = mid - 1
        return -1

