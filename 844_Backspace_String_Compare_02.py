# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # define two pointers and move backwards
        i = len(s) - 1 # indices
        j = len(t) - 1

        skipS = skipT = 0 # two pointers

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    skipS += 1 # we need to skip next character to the left
                    i -= 1 # index moving backwards
                elif skipS > 0: # meaning we saw one #
                    skipS -= 1 # skip the character to the left
                    i -= 1
                else:
                    break # stop this while loop immediately

            while j >= 0:
                if t[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break

            # compare values - right before this, we already skipped all # and delete characters
            # we landed on the next valid characters on both strings
            if i >= 0 and j >= 0: # at this point, backspace and deletion have been done, both sides clean
                # case 1: both pointers are valid
                if s[i] != t[j]:
                    return False
            # case 2: only one string has characters left
            elif i >= 0 or j >= 0:
                return  False
        
            # move the pointer to the left for the next comparison
            i -= 1
            j -= 1
        
        return True
    
# Time: O(m + n) where m, n are the lengths for s and t respectively; even though we have nested while loop,
# each character is visted at most once
# Space: O(1) we only use two pointers i, j and two counters, skipS and skipT, no extra data structure is created with the input size (e.g. arrays, stacks etc)
 
    





