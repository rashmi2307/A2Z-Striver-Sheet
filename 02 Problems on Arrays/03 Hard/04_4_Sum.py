# Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# a, b, c, d are all distinct valid indices of nums.
# nums[a] + nums[b] + nums[c] + nums[d] == target.

# Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets. The output and the quadruplets can be returned in any order.

# Example 1
# Input: nums = [1, -2, 3, 5, 7, 9], target = 7
# Output: [[-2, 1, 3, 5]]
# Explanation:
# nums[1] + nums[0] + nums[2] + nums[3] = 7

# Example 2
# Input: nums = [7, -7, 1, 2, 14, 3], target = 9
# Output: []
# Explanation:
# No quadruplets are present which add upto 9




# Brute Force Approach : Time Limit Exceeded
# Time Complexity: O(n^4) where n is the length of the input array
from git import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        n = len(nums)
        for i in range (n):
            for j in range (i+1, n):
                for k in range (j+1 ,n):
                    for l in range (k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            triplet = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))     
                            answer.add(triplet)   
        return [list(triplet) for triplet in answer]
    



# Better Approach
# Time Complexity: O(n^3 * log (no. of unique quadruplets)) where n is the length of the input array
# Space Complexity: O(n)+O(2*no. of unique quadruplets) as we are using a set to store the result
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        n = len(nums)
        for i in range (n):
            for j in range (i+1, n):
                seen = set()
                for k in range (j+1 ,n):
                    fourth = target - (nums[i] + nums[j]+ nums[k])
                    if fourth in seen:
                        quad = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                        answer.add(quad)
                    seen.add(nums[k])
        return [list(quad) for quad in answer]
    




# Optimal Approach
# Time Complexity: O(n^3) where n is the length of the input array
# Space Complexity: O(1) as we are not using any extra space
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(nums)
        nums.sort()
        for i in range (n):
            if i> 0 and nums[i] == nums[i-1]:
                continue

            for j in range (i+1, n):
                if j> i+1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
    
                    if total == target:
                        answer.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return answer


