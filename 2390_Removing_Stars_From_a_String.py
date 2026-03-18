# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters and stars *.
# The operation above can be performed on s.

# What we want:
# 1) if ch is a letter, push it onto the stack
# 2) if ch is '*' pop the previous letter

class Solution:
    def remove_stars(self, s:str) -> str:
        stack = []

        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)
    
# Time: O(n) for n is the number of characters in string
# Space: O(n) stack can grow up to n
