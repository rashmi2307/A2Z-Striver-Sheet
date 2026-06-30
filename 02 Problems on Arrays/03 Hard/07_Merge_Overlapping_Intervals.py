# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

# You can return the intervals in any order.

# Example 1
# Input: intervals = [[1,5],[3,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Intervals [1,5] and [3,6] overlap, so they are merged into [1,6].

# Example 2
# Input: intervals = [[5,7],[1,3],[4,6],[8,10]]
# Output: [[1,3],[4,7],[8,10]]
# Explanation: Intervals [4,6] and [5,7] overlap and are merged into [4,7].




# Brute Force Approach 
# Time Complexity: O(n^2) where n is the length of the input array
from ast import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        n = len(intervals)
        i = 0
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]
            j = i+1
            while j < n and intervals[j][0] <=end:
                end = max(end,intervals[j][1])
                j += 1
            answer.append([start,end])
            i = j
        return answer
    





