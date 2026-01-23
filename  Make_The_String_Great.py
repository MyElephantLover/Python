# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

# Notice that an empty string is also good.

# Constraints:

# 1 <= s.length <= 100
# s contains only lower and upper case English letters.

class Solution:
    def makeStringGreat(self, s: str) -> str:
        stack = [] # the stack stores the current 'good' version of the string you built so far

        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append()

        return ''.join(stack)
    
# ASCII value is computer systems use to store characters
# characters with different cases have difference of 32 in ASCII values
# ord() is used to map characters to ASCII values
# use abs() because we are not sure which one is bigger

# Time Complexity: O(n) we iterate over the string once
# Space Complexity: O(n)
    
