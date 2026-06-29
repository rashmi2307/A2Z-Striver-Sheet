# Given an integer array nums. Return all triplets such that:

# i != j, i != k, and j != k
# nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets. The output and the triplets can be returned in any order.

# Example 1
# Input: nums = [2, -2, 0, 3, -3, 5]
# Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]
# Explanation:
# nums[1] + nums[2] + nums[0] = 0
# nums[4] + nums[1] + nums[5] = 0
# nums[4] + nums[2] + nums[3] = 0

# Example 2
# Input: nums = [2, -1, -1, 3, -1]
# Output: [[-1, -1, 2]]
# Explanation:
# nums[1] + nums[2] + nums[0] = 0
# Note that we have used two -1s as they are separate elements with different indexes
# But we have not used the -1 at index 4 as that would create a duplicate triplet




# Brute Force Approach : Time Limit Exceeded
# Time Complexity: O(n^3) where n is the length of the input array
# Space Complexity: O(n) as we are using a set to store the result
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        st = set()
        for i in range (n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i],nums[j],nums[k]]))
                        st.add(triplet)
        return [list(triplet) for triplet in st]
    




# Better Approach
# Time Complexity: O(n^2 * log (no. of unique triplets)) where n is the length of the input array
# Space Complexity: O(n)+O(2*no. of unique triplets) as we are using a set to store the result
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        answer = set()
        for i in range (n):
            seen = set()
            for j in range (i+1,n):
                third = -(nums[i]+nums[j])
                if third in seen:
                    triplet = tuple(sorted([nums[i],nums[j],third]))
                    answer.add(triplet)
                seen.add(nums[j])
        return [list (t) for t in answer]




# Optimal Solution: Use Hashnet and 2 pointers to find the triplets that sum up to 0. Sort the array and use a for loop to iterate through the array. For each element, use two pointers to find the other two elements that sum up to 0. Skip duplicates to avoid duplicate triplets in the answer.    
# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(n) as we are using a list to store the result
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        answer = []
        nums.sort()
        for i in range (n):
            if nums[i] == nums[i-1] and i > 0:
                continue
            left = i + 1
            right =  n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return answer