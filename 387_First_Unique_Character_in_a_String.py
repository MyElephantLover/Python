# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.

class Solution:
    def uniqueCharacter(self, s: str) -> int:
        seen = {}

        # step1: count freq of each character
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        # step2: find the first character with count 1
        for i, ch in enumerate(s):
            if seen[ch] == 1:
                return i
            
        return -1
    
# Time: O(n) each character is visited once
# Space: O(1) there are at most 26 possible keys regardless how long the string isS

