# Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.

# Example 1
# Input : nums =[3, 4, 4, 7, 8, 10], x= 5
# Output: 4 7
# Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

# Example 2
# Input : nums =[3, 4, 4, 7, 8, 10], x= 8
# Output: 8 8
# Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.



# Iterative Approach:
# Time Complexity: O(log n) - We are iterating through the entire array to find the floor and ceil of the target integer.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def getFloorAndCeil(self, nums, x):
        floor = self.getFloor(nums,x)
        ceil = self.getCeil(nums,x)
        return floor, ceil

    def getCeil(self,nums, x):
        answer = -1
        low = 0
        high  = len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid] >= x:
                answer = nums[mid]
                high = mid - 1
            else:
                low = mid + 1
        return answer

    def getFloor(self,nums,x):
        answer = -1
        low = 0
        high = len(nums) -1
        while low <= high :
            mid = (low + high) // 2
            if nums[mid] <= x :
                answer = nums[mid]
                low = mid+1
            else:
                high = mid-1
        return answer