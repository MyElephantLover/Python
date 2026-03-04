# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != mapping[ch]: # the last opening bracket does not match the expected type
                    return False
                stack.pop() # remove the most recent value in the stack

        return len(stack) == 0 # this block runs after the entire string has been processed, it ensures no unmatched brackets remain
    
# Time: O(n) as we traverse each character in the string
# Space: O(n) in worst case, the string contains all opening brackets - since the stack stores opening brackets






