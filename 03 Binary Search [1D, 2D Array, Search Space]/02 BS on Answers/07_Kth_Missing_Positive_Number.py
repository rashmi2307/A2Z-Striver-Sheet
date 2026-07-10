# Given a sorted array of unique positive integers arr, your task is to return the kᵗʰ missing positive number that is not present in arr.

# The array is guaranteed to be strictly increasing, and the missing numbers are those positive integers that do not appear in arr but would appear in a full sequence starting from 1.

# Example 1
# Input: arr = [3, 5, 7, 10], k = 6
# Output: 9
# Explanation:
# The missing numbers are [1, 2, 4, 6, 8, 9, 11, ...]. The 6ᵗʰ missing number is 9.

# Example 2
# Input: arr = [1, 4, 6, 8, 9], k = 3
# Output: 5
# Explanation:
# The missing numbers are [2, 3, 5, 7, 10, ...]. The 3ʳᵈ missing number is 5.




# Brute Force Approach: My Own
# Time Complexity: O(n) - We are iterating through the entire array.
# Space Complexity: O(1) - We are not using any extra space.
from ast import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        for i in range (len(arr) + k+1):
            if i not in arr:
                missing.append(i)
            
        return missing[k]





# Brute Force Approach:
# Time Complexity: O(n) - We are iterating through the entire array.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k
    



