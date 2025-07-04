class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Horizonal scanning following the logics described in the solution in Java

        # First, consider the edge case - if strs is none, return ""

        if len(strs) == 0:
            return ""
        
        # initialize prefix as strs[0]

        prefix = strs[0]

        # loop through the rest of the string, from the second character (index 1) to check
        # if the current prefix matches with strs[i]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0: # this is trying to find the position of the prefix in strs
                prefix = prefix[0: len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix
    
# Time Complexity: O(S) while S is the sum of all the characters in all the strings
# Space Complexity: O(1) we only used constant extra space



