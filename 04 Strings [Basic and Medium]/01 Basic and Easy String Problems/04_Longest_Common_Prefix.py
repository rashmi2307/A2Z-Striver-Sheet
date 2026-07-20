# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1
# Input : str = ["flowers" , "flow" , "fly", "flight" ]
# Output : "fl"
# Explanation :
# All strings given in array contains common prefix "fl".

# Example 2
# Input : str = ["dog" , "cat" , "animal", "monkey" ]
# Output : ""
# Explanation :
# There is no common prefix among the given strings in array.





from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if not strs:
            return ""
        
        strs.sort()

        first = strs[0]
        last = strs[-1]

        ans = []

        for i in range (min(len(first), len(last))):
            if first[i] != last[i]:
                return "".join(ans)
            ans.append(first[i])
        return "".join(ans)