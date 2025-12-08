# Given a string s, reverse the order of characters in each word within a sentence 
# while still preserving whitespace and initial word order.

# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

class Solution:
    def reverseWords(self, s:str) -> str:
        # We could use two pointers, startIndex, endIndex to track the start and end point of the current words
        # and reverse each word while travering the string
        words = s.split() # split the string, s, into a list of words
        reversed_str = '' # initialize an empty string to store the result set
        # it mentions no trailing and leading spaces
        # loop through the list of words
        for word in words:
            reversed_str += word[::-1] + ' ' # traverse backwards and add a single space as the separator
        return reversed_str.strip() # use strip() method to remove leading or trailing spaces, not affecting spaces in the middle
    
# Time Complexity: O(n) where n is the length of the string, s. The outer loop traverse the whole string once, and reversing
# each word also iterate n times to perform n/2 swaps. Hence, it is O(n+n) = O(n)
# Space: O(1) 
     