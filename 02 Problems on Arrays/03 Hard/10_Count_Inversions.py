# Given an integer array nums. Return the number of inversions in the array.
# Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

# It indicates how close an array is to being sorted.
# A sorted array has an inversion count of 0.

# An array sorted in descending order has maximum inversion.

# Example 1
# Input: nums = [2, 3, 7, 1, 3, 5]
# Output: 5
# Explanation:
# The responsible indexes are:
# nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3
# nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3
# nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3
# nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4
# nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5

# Example 2
# Input: nums = [-10, -5, 6, 11, 15, 17]
# Output: 0
# Explanation:
# nums is sorted, hence no inversions present.



# Brute Force Approach: Time Limit exceeded for large inputs. We can optimize this using merge sort technique.
# Time Complexity: O(n^2) where n is the length of the input array
class Solution:
    def numberOfInversions(self, nums):
        n = len(nums)
        count = 0
        for i in range (n):
            for j in range (i+1,n):
                if nums[j] < nums[i]:
                    count += 1
        return count
    



# Optimized Approach: Using merge sort technique. 
# Time Complexity: O(nlogn) where n is the length of the input array

class Solution:
    def numberOfInversions(self, nums) -> int:
        return self.sort(nums,0,len(nums)-1)

    def sort(self,nums,low,high) -> int:
        count = 0
        if low>=high:
            return count
        mid = (low+high)//2
        count += self.sort(nums,low, mid)
        count += self.sort(nums,mid+1,high)
        count += self.merge(nums,low,mid,high)
        return count

    def merge(self,nums,low,mid,high) -> int:
        temp = []
        left = low
        right = mid + 1
        count = 0
        while left<=mid and right <=high:
            if nums[left] <=nums[right]:
                temp.append(nums[left])
                left+=1
            # right is smaller
            else:
                temp.append(nums[right])
                count += (mid - left + 1)
                right+=1
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=high:
            temp.append(nums[right])
            right+=1
        for x in range (low,high+1):
            nums[x] = temp[x-low]
        return count