# Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once.

# Return the number of unique elements in the array.

# If the number of unique elements be k, then,

# Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
# The remaining elements, as well as the size of the array does not matter in terms of correctness.
# The driver code will assess correctness by printing and checking only the first k elements of the modified array.

# An array sorted in non-decreasing order is an array where every element to the right of an element is either equal to or greater in value than that element.



class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = i+1
        while j < len(nums):
            if nums[j] == nums[i]:
                j+=1
            else:
                nums[i+1] = nums[j]
                i+=1
                j+=1
        return i+1
    

# Notes:
# Use two pointers i and j.
# i points to the last unique element, j traverses the array.
# If nums[j] == nums[i], j is a duplicate, so we move j forward.
# If nums[j] != nums[i], we found a new unique element, so we move i forward and copy nums[j] to nums[i].
# Time: O(n), Space: O(1). ✅