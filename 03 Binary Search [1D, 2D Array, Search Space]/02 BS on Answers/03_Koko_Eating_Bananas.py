# A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas. An integer h represents the total time in hours to eat all the bananas.

# Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. If the pile contains fewer than k bananas, the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.

# Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.

# Example 1
# Input: n = 4, nums = [7, 15, 6, 3], h = 8
# Output: 5
# Explanation: If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.  

# Example 2
# Input: n = 5, nums = [25, 12, 8, 14, 19], h = 5
# Output: 25
# Explanation: If Koko eats 25 bananas/hr, he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly. So, he will take 5 hours to complete all the piles.





# Brute Force Approach:
# Time Complexity: O(n * max(piles)) - We are iterating through the entire array and for each element we are calculating the total hours required to eat all the bananas.
# Space Complexity: O(1) - We are not using any extra space.
from ast import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxVal = max(piles)
        for i in range (1, maxVal+1):
            hours = self.calculateTotalHours(piles,i)
            if hours <= h:
                return i
        return maxVal


    def calculateTotalHours(self, piles: List[int], hourly: int) -> int:
        totalHours = 0
        for pile in piles:
            totalHours += math.ceil(pile/hourly)
        return totalHours