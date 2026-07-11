# Given an integer array a of size n and an integer k. Split the array a into k non-empty subarrays such that the largest sum of any subarray is minimized. Return the minimized largest sum of the split.

# Example 1
# Input: a = [1, 2, 3, 4, 5], k = 3
# Output:6
# Explanation: There are many ways to split the array a[] into k consecutive subarrays. The best way to do this is to split the array a[] into [1, 2, 3], [4], and [5], where the largest sum among the three subarrays is only 6.

# Example 2
# Input: a = [3,5,1], k = 3
# Output: 5
# Explanation: There is only one way to split the array a[] into 3 subarrays, i.e., [3], [5], and [1]. The largest sum among these subarrays is 5.





# Brute Force Approach:
# Time Complexity: O(n * m) - We are iterating through the entire array for each possible maximum sum, where m is the sum of the array.
# Space Complexity: O(1) - We are not using any extra space.
class SubarrayPartitioner:
    # Counts how many partitions are needed given maxSum
    def count_partitions(self, a, max_sum):
        partitions = 1  # at least one partition
        subarray_sum = 0  # current subarray sum

        for num in a:
            # Add to current subarray if it doesn't exceed max_sum
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                # Start a new subarray
                partitions += 1
                subarray_sum = num
        return partitions

    # Finds the smallest possible largest subarray sum for exactly k partitions
    def largest_subarray_sum_minimized(self, a, k):
        low = max(a)  # minimum possible max sum
        high = sum(a)  # maximum possible max sum

        # Brute-force check
        for max_sum in range(low, high + 1):
            if self.count_partitions(a, max_sum) == k:
                return max_sum
        return low  # fallback




# Optimized Approach:
# Time Complexity: O(n log m) - We are using binary search to find the minimum largest sum of the split. The binary search will take log m time, where m is the sum of the array. For each mid value, we are iterating through the entire array to count the number of partitions, which will take O(n) time.
# Space Complexity: O(1) - We are not using any extra space.
from git import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1
        
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = low + (high - low)//2 
            partitions = self.countPartitions(nums, mid)
            if partitions > k:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def countPartitions(self,nums, max_sum):
        partitions = 1
        subarray_sum = 0
        for num in nums:
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                partitions += 1
                subarray_sum = num
        return partitions
    