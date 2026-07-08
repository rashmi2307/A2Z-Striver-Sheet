# Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).

# Example 1
# Input: n = 36
# Output: 6
# Explanation: 6 is the square root of 36.

# Example 2
# Input: n = 28
# Output: 5
# Explanation: The square root of 28 is approximately 5.292. So, the floor value will be 5.




# Time Complexity: O(sqrt(n)) - We are iterating through the numbers from 1 to n to find the square root.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def floorSqrt(self, n: int) -> int:
        large = 0
        for i in range (1, n+1):
            if i*i <= n:
                large = i
            else:
                break
        return large 




# Time Complexity: O(log n) - We are using binary search to find the square root.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def floorSqrt(self, n: int) -> int:
        if n < 2:
            return n
        left, right, answer = 0, n//2, 0
        while left <= right:
            mid = (left + right)// 2
            if mid*mid <= n:
                answer = mid
                left = mid+1
            else:
                right = mid-1
        return answer

