# You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.

# Return the count of occurrences of target in the array.

# Example 1
# Input: arr = [0, 0, 1, 1, 1, 2, 3], target = 1
# Output: 3
# Explanation: The number 1 appears 3 times in the array.

# Example 2
# Input: arr = [5, 5, 5, 5, 5, 5], target = 5
# Output: 6
# Explanation: All elements in the array are 5, so the target appears 6 times.




# Brute Force Approach:
# Time Complexity: O(n) - We are iterating through the entire array to count the occurrences of the target integer.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def countOccurrences(self, arr, target):
        n = len(arr)
        count = 0
        for i in range (n):
            if target == arr[i]:
                count += 1
        return count
    

# Binary Search Approach:
# Time Complexity: O(log n) - We are iterating through the entire array to find the first and last occurrence of the target integer.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def countOccurrences(self, arr, target):
        first = self.getFirst(arr, target)
        last = self.getLast(arr, target)
        if first == -1:
            return 0
        else:
            return (last - first + 1)

    def getFirst(self,arr,target):
        answer = -1
        low = 0
        high = len(arr) -1
        while low <= high :
            mid = (low + high) // 2
            if arr[mid] == target:
                answer = mid
                high = mid - 1
            elif arr[mid] < target :
                low = mid + 1
            elif arr[mid] > target :
                high = mid -1
        return answer

    def getLast(self,arr, target):
        answer = -1
        low = 0
        high  = len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid] == target:
                answer = mid
                low = mid + 1
            elif arr[mid] < target :
                low = mid + 1
            elif arr[mid] > target :
                high = mid -1
        return answer