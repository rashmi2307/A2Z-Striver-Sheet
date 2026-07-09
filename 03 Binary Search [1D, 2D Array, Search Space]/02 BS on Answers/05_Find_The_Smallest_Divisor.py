# Given an array of integers nums and an integer limit as the threshold value, find the smallest positive integer divisor such that upon dividing all the elements of the array by this divisor, the sum of the division results is less than or equal to the threshold value.

# After dividing each element by the chosen divisor, take the ceiling of the result (i.e., round up to the next whole number).

# Example 1
# Input: nums = [1, 2, 3, 4, 5], limit = 8
# Output: 3
# Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
# The sum is 9(1 + 1 + 2 + 2 + 3) if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

# Example 2
# Input: nums = [8,4,2,3], limit = 10
# Output: 2
# Explanation: If we choose 1, we get 17 as the sum. If we choose 2, we get 9 (4+2+1+2) <= 10 as the answer. So, 2 is the answer.





# Brute Force Approach:
# Time Complexity: O(n * max(nums)) - We are iterating through the entire array
# Space Complexity: O(1) - We are not using any extra space.
from ast import List
from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        for divisor in range (1, max(nums)+1):
            sum = 0
            for i in range (len(nums)):
                sum += ceil(nums[i]/divisor)
            if sum <=threshold:
                return divisor
        return -1
    




# Optimized Approach:
# Time Complexity: O(n * log(max(nums))) - We are iterating through the entire array and for each divisor we are checking if it is possible to get the sum less than or equal to threshold.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        if len(nums) > threshold:
            return -1

        low = 1
        high = max(nums) 

        while low <= high:
            mid = (low+high)//2
            if self.sumByD(nums, mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low


    def sumByD(self, nums, divisor):
        return sum(ceil(x/divisor) for x in nums)

