# Given n roses and an array nums where nums[i] denotes that the 'ith' rose will bloom on the nums[i]th day, only adjacent bloomed roses can be picked to make a bouquet. Exactly k adjacent bloomed roses are required to make a single bouquet. Find the minimum number of days required to make at least m bouquets, each containing k roses. Return -1 if it is not possible.

# Example 1
# Input: n = 8, nums = [7, 7, 7, 7, 13, 11, 12, 7], m = 2, k = 3
# Output: 12
# Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

# Example 2
# Input: n = 5, nums = [1, 10, 3, 10, 2], m = 3, k = 2
# Output: -1
# Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 flowers. But we are given only 5 flowers, so, we cannot make the bouquets.




# Brute Force Approach:
# Time Complexity: O(n * (max(bloomDay) - min(bloomDay))) - We are iterating through the entire array and for each day we are checking if it is possible to make m bouquets.
# Space Complexity: O(1) - We are not using any extra space.
from git import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        total_flowers = m*k
        if total_flowers > len(bloomDay):
            return -1
        
        low = min(bloomDay)
        high = max(bloomDay)


        for day in range (low, high + 1):
            if self.is_possible(bloomDay, day, m , k):
                return day
        return -1
        
    
    def is_possible(self, bloom_days, day, m, k):
        count = 0
        bouquets = 0

        for bloom in bloom_days:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0
        return bouquets >= m
    



# Optimized Approach:
# Time Complexity: O(n * log(max(bloomDay) - min(bloomDay))) - We are using binary search to find the minimum number of days required to make m bouquets. For each mid value, we are checking if it is possible to make m bouquets.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        total_flowers = m*k
        if total_flowers > len(bloomDay):
            return -1
        
        answer = -1
        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            mid = (low+high)//2
            if self.is_possible(bloomDay, mid, m, k):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer

    
    def is_possible(self, bloom_days, day, m, k):
        count = 0
        bouquets = 0

        for bloom in bloom_days:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0
        return bouquets >= m
