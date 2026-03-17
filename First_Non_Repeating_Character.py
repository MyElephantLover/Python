# Given a string, return the first character that appears only once.

# Examples:

# "swiss" → "w"

# "aabb" → None


class Solution:
    def firstNonRepeatingCharacter(self, s:str) -> str:
        count = {}

        # step1: count frequency
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # step2: find first unique ch
        for ch in s:
            if count[ch] == 1:
                return ch
            
        return None

# Time: O(n) for n is the number of characters in the string s - we do two passes over the string:
# the first counts the frequency; the second to find the first unique
# Space: O(n) in the worst case, every character in the string is unique - dictionary stores all characters



