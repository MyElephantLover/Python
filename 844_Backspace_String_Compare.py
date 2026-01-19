# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
 
# Follow up: Can you solve it in O(n) time and O(1) space?

class Solution:
    def backspaceString(self, s:str, t:str) -> bool:

        def process(): # use a helper function
            stack = []

            for ch in s:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)

        return process(s) == process(t) # we wanted to check if after removing backspace, the two string equals
    
class Solution:
    def backspaceString(self, s: str, t: str) -> bool:

        # initiate two indices from both strings
        i = len(s) - 1
        j = len(t) - 1

        skipS = skipT = 0 # two pointers marking the skip pace

        while i >= 0 or j >= 0:

            while i >= 0:
                if s[i] == "#":
                    skipS += 1 # we need to skip backspace "a#bc" - skipS increment a counter for scanning from the right
                    # take "a#bc" as an exmple, when we reach #, we skip a - the character to the left of #
                    i -= 1 
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0: # when skipT == 1 means we see #
                    skipT -= 1 # means one deletion has been applied
                    j -= 1
                else:
                    break

            # compare characters
            if i >= 0 and j >= 0: # we left with the cleaned strings w/o # and done deletion
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
                
            i -= 1
            j -= 1

        return True


# Time Complexity: O(n) where n is the total of input sizes = length of s and length of t
# Space Complexity: O(1) two-pointers scans backwards without using extra memory 

