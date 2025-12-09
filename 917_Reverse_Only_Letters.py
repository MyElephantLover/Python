# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

# Constraints:

# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.

class Solution:
    reverseLetters(self, s:str) -> str:
    # create a list with all characters in the string s

    letters = [c for c in s if c.isalpha()]

    # create an empty string ans to store the answer and convert to string later
    ans = []

    for c in s: # loop through every character in s
        if c.isalpha(): # c is an English word, we need to pop() it out of letters and append to the ans list from the start
            ans.append(letters.pop())
        else:
            ans.append(c) # other character remain the same position in s
    return "".join(ans)

# Time Complexity: O(n) where n is the length of the string s because we iterate over every character in s
# Space Complexity: O(n) because we created a string with join() and a string is immutable so we allocated new memory

