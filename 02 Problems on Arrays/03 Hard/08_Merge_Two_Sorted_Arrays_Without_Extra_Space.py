# Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.
# Merge both the arrays into a single array sorted in non-decreasing order.

# The final sorted array should be stored inside the array nums1 and it should be done in-place.

# nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
# nums2 has a length of n.

# Example 1
# Input: nums1 = [-5, -2, 4, 5], nums2 = [-3, 1, 8]
# Output: [-5, -3, -2, 1, 4, 5, 8]
# Explanation:
# The merged array is: [-5, -3, -2, 1, 4, 5, 8], where [-5, -2, 4, 5] are from nums1 and [-3, 1, 8] are from nums2

# Example 2
# Input: nums1 = [0, 2, 7, 8], nums2 = [-7, -3, -1]
# Output: [-7, -3, -1, 0, 2, 7, 8]
# Explanation:
# The merged array is: [-7, -3, -1, 0, 2, 7, 8], where [0, 2, 7, 8] are from nums1 and [-7, -3, -1] are from nums2




# Time Complexity: O(m+n) where m and n are the lengths of the input arrays
from git import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1



# Without Extra Space
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                m += 1
                print(i,j,m, nums1)
            else:
                i += 1
                print(i,j,m, nums1)
        while j < n:
            nums1.extend([nums2[j]])
            j += 1