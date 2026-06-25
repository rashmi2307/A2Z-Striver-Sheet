# Given an array nums of n integers.

# Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.

# Example 1
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation:
# The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. This sequence can be formed regardless of the initial order of the elements in the array.

# Example 2
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9
# Explanation:
# The longest sequence of consecutive elements in the array is [0, 1, 2, 3, 4, 5, 6, 7, 8], which has a length of 9. 


# Optimal Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) as we are storing all the elements of the input array in
from git import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest = 1
        st = set()
        for i in range (len(nums)):
            st.add(nums[i])
        for it in st:
            if it - 1 not in st:
                count = 1
                x = it
                while x + 1 in st:
                    count +=1
                    x+=1
                if count > longest:
                    longest = count
        return longest