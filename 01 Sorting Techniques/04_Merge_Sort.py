# Given an array of integers, nums,sort the array in non-decreasing order using the merge sort algorithm. Return the sorted array.

# A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.

# Example 1 Input: nums = [7, 4, 1, 5, 3] Output: [1, 3, 4, 5, 7]

# Explanation: 1 <= 3 <= 4 <= 5 <= 7. Thus the array is sorted in non-decreasing order.

# Example 2 Input: nums = [5, 4, 4, 1, 1] Output: [1, 1, 4, 4, 5]

# Explanation: 1 <= 1 <= 4 <= 4 <= 5. Thus the array is sorted in non-decreasing order.



# Only nums as parameter
class Solution:
    def mergeSort(self, nums):
        self.sort(nums,0, len(nums)-1)
        return nums

    def sort(self,nums,low,high):
        if low>=high:
            return
        mid = (low+high)//2
        self.sort(nums,low, mid)
        self.sort(nums,mid+1,high)
        self.merge(nums,low,mid,high)

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
        for x in temp:
            nums[low] = x
            low+=1
                



# nums, low, high parameters
class Solution:
    def mergeSort(self, nums, low, high):
        if low>=high:
            return
        mid = (low+high)//2
        self.mergeSort(nums,low, mid)
        self.mergeSort(nums,mid+1,high)
        self.merge(nums,low,mid,high)
        return nums

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
        for x in temp:
            nums[low] = x
            low+=1
        return nums
