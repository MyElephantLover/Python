# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def validParentheses(self, s : str) -> bool:
        stack = []
        mapping = {'(':')', '{':'}', '[':']'}

        for ch in s:
            if ch in mapping.values():
                stack.append(ch) # stack stores opening brackets
            else:
                if not stack or stack[-1] != mapping[ch]: # mapping[ch] can be any part of parentheses
                    return False 
                stack.pop()

        return len(stack) == 0 # stack must be empty for a valid string

# Time Complexity: O(n) for iterating every character in the string
# Space Complexity: O(n) for worst case all opening brackets