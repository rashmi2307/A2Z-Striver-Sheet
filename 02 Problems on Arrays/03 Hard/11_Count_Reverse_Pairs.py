# Given an integer array nums. Return the number of reverse pairs in the array.
# An index pair (i, j) is called a reverse pair if:

# 0 <= i < j < nums.length
# nums[i] > 2 * nums[j]

# Example 1
# Input: nums = [6, 4, 1, 2, 7]
# Output: 3
# Explanation:
# The reverse pairs are:
# (0, 2) : nums[0] = 6, nums[2] = 1, 6 > 2 * 1
# (0, 3) : nums[0] = 6, nums[3] = 2, 6 > 2 * 2
# (1, 2) : nums[1] = 4, nums[2] = 1, 4 > 2 * 1

# Example 2
# Input: nums = [5, 4, 4, 3, 3]
# Output: 0
# Explanation:
# No pairs satisfy both the conditons.




# Brute Force Approach: Time Limit exceeded for large inputs. We can optimize this using merge sort technique.
# Time Complexity: O(n^2) where n is the length of the input array
from ast import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range (n):
            for j in range (i+1,n):
                if nums[i] > 2* nums[j]:
                    count += 1
        return count
    



# Optimized Approach: Using merge sort technique to count the reverse pairs.
# Time Complexity: O(nlogn) where n is the length of the input array
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.sort(nums,0,len(nums)-1)

    def sort(self,nums,low,high) -> int:
        count = 0
        if low>=high:
            return count
        mid = (low+high)//2
        count += self.sort(nums,low, mid)
        count += self.sort(nums,mid+1,high)
        count += self.countPairs(nums,low,mid,high)
        self.merge(nums, low, mid, high)
        return count

    def merge(self,nums,low,mid,high):
        temp = []
        left = low
        right = mid + 1
        while left<=mid and right <=high:
            if nums[left] <=nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=high:
            temp.append(nums[right])
            right+=1
        for i in range (low, high + 1):
            nums[i] = temp[i - low]

    def countPairs (self,nums, low, mid, high)-> int:
        count = 0
        right = mid + 1
        for i in range (low,mid + 1):
            while (right <=high and nums[i]>nums[right]*2):
                right += 1
            count += right - (mid + 1)
        return count