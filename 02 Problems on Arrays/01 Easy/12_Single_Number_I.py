# Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.

# Example 1
# Input : nums = [1, 2, 2, 4, 3, 1, 4]
# Output : 3
# Explanation : The integer 3 has appeared only once.

# Example 2
# Input : nums = [5]
# Output : 5
# Explanation : The integer 5 has appeared only once.


# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(n) as we are using a temporary list to store the unique elements
class Solution:
    def singleNumber(self, nums):
        #your code goes here
        temp = []
        for i in range(len(nums)):
            if nums[i] in temp:
                temp.remove(nums[i])
            else:
                temp.append(nums[i])
        return temp[0]
            


# Optimal Solution using XOR operator
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the result of XOR operation


class Solution:
    def singleNumber(self, nums):
        #your code goes here
        XOR = 0
        for i in range(len(nums)):
            XOR = XOR ^ nums[i]
        return XOR