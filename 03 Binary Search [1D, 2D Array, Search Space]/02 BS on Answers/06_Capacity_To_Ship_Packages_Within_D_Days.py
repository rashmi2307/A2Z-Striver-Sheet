# You are given an array weights where weights[i] represents the weight of the i-th package on a conveyor belt. All the packages must be shipped in the order given from one port to another within days days.

# Each day, the ship can carry a contiguous sequence of packages, as long as the total weight does not exceed its maximum capacity.

# Your task is to find the minimum possible capacity of the ship so that all packages can be shipped within the given number of days.

# Example 1
# Input: weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
# Output: 15
# Explanation:
# Minimum ship capacity = 15. One way to ship in 5 days:
# Day 1: 1 + 2 + 3 + 4 + 5 = 15
# Day 2: 6 + 7 = 13
# Day 3: 8
# Day 4: 9
# Day 5: 10
# No day exceeds capacity 15 and all packages are shipped in order in 5 days.

# Example 2
# Input: weights = [3, 2, 2, 4, 1, 4], days = 3
# Output: 6
# Explanation:
# One possible division with capacity 6:
# Day 1: 3 + 2 = 5
# Day 2: 2 + 4 = 6
# Day 3: 1 + 4 = 5
# All packages shipped in order within 3 days.





# Brute Force Approach:
# Time Complexity: O(n * max(weights)) - We are iterating through the entire array
# Space Complexity: O(1) - We are not using any extra space.
from ast import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        for capacity in range (max(weights), sum(weights)+1):
            daysRequired = int(self.daysNeeded(weights, capacity))
            if daysRequired <= days:
                return capacity
        return sum(weights)

    def daysNeeded(self, weights, capacity):
        days = 1
        currentLoad = 0
        for w in weights:
            if currentLoad + w > capacity:
                days += 1
                currentLoad = w
            else:
                currentLoad += w
        return days
    



# Optimized Approach:
# Time Complexity: O(n * log(sum(weights) - max(weights))) - We are iterating through the entire array and for each capacity we are checking if it is possible to get the sum less than or equal to days.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        answer = right

        while left <= right:
            mid = left + (right - left)//2
            daysRequired = int(self.daysNeeded(weights, mid))
            if daysRequired <= days:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer

    def daysNeeded(self, weights, capacity):
        days = 1
        currentLoad = 0

        for w in weights:
            if currentLoad + w > capacity:
                days += 1
                currentLoad = w
            else:
                currentLoad += w
        return days