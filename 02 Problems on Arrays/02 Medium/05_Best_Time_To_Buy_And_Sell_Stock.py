# Given an array arr of n integers, where arr[i] represents price of the stock on the ith day. Determine the maximum profit achievable by buying and selling the stock at most once. 

# The stock should be purchased before selling it, and both actions cannot occur on the same day.

# Example 1
# Input: arr = [10, 7, 5, 8, 11, 9]
# Output: 6
# Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.

# Example 2
# Input: arr = [5, 4, 3, 2, 1]
# Output: 0
# Explanation: In this case, no transactions are made. Therefore, the maximum profit remains 0.



# Brute Force Approach
# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the maximum
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = 0
        for i in range (n):
            for j in range (i+1, n):
                profit = prices[j] - prices[i]
                maxprofit = max(profit, maxprofit)
        return maxprofit




# Optimal Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the maximum
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            if prices[i] - mini > maxprofit:
                maxprofit = prices[i] - mini
        return maxprofit