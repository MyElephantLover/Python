# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

# Constraints:

# 1 <= s.length <= 1e5
# s consists of lowercase English letters.

class Solution:
    def removeDuplicate(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop() # remove duplicated pair
            else:
                stack.append(ch) # keep it

        return "".join(stack) # convert list to string
    
# Time Complexity: O(n) for n up to 1e5 (10 to the power of 5) -> the constraint
# Space Complexity: O(n) worst case