# Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.
# Return a string with the words in reverse order, concatenated by a single space.

# Example 1
# Input: s = "welcome to the jungle"
# Output: "jungle the to welcome"
# Explanation: The words in the input string are "welcome", "to", "the", and "jungle". Reversing the order of these words gives "jungle", "the", "to", and "welcome". The output string should have exactly one space between each word.

# Example 2
# Input: s = " amazing coding skills "
# Output: "skills coding amazing"
# Explanation: The input string has leading and trailing spaces, as well as multiple spaces between the words "amazing", "coding", and "skills". After trimming the leading and trailing spaces and reducing the multiple spaces between words to a single space, the words are "amazing", "coding", and "skills". Reversing the order of these words gives "skills", "coding", and "amazing". The output string should not have any leading or trailing spaces and should have exactly one space between each word.



# Brute Force Approach:
# 1. Split the input string into words using the split() method, which automatically handles multiple spaces and trims leading/trailing spaces.
# 2. Reverse the list of words using slicing or the reverse() method.
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for char in s:
            if char != " ":
                word += char
            elif word:
                words.append(word)
                word = ""
        if word:
            words.append(word)

        words.reverse()

        return " ".join(words)



# Optimal Approach:
# 1. Initialize an empty string result to store the reversed words.
# 2. Use a pointer to traverse the input string from the end to the beginning.
# 3. Skip any trailing spaces by moving the pointer backward until a non-space character is found.
# 4. Identify the end of the current word by storing the pointer's position.
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        pointer = len(s)-1
        while pointer >= 0:
            while pointer >= 0 and s[pointer] == " ":
                pointer -= 1
            if pointer < 0:
                break
            end = pointer

            while pointer >= 0 and s[pointer] != " ":
                pointer -= 1
            
            word = s[pointer+1:end+1]

            if result != "":
                result += " "

            result += word

        return result
       