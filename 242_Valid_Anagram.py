# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def anagram(self, s: str, t: str) -> bool:
        # idea for an anagram is:
        # 1) if two strings are anagrams, they must have the same length
        # 2) every character must appear the same number of times
        # so we need to use Character Frequency Count (dictionary)

        # edge case
        if len(s) != len(t):
            return False
        
        # create a dictionary
        # count is the dictionary storing how many times each character appear in s
        count = {}

        # count character in s
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Subtract using t
        for char in t:
            if char not in count:
                return False
            # otherwise we calculate frequency
            count[char] -= 1
            if count[char] == 0:
                del count[char] # we remove this char in count because its count is fully matched

        # at the end, if s and t are anagrams, these criterias are met:
        # 1) each character frequency will be reduced to 0
        # 2) every key will be deleted
        # 3) the dictionary becomes empty 

        return len(count) == 0 # we check whether the dictionay is empty
    
# Time Complexity: O(n) we checked each character in s so we went through the size of the string n
# Space Complexity: O(1) there is 26 lowercase English letters

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# What changed: we can't assume a fixed alphabet size(like 26 lowercase letters),so space is no longer constant
# space complexity becomes O(k) where k is the number of distinct characters across s and t (worst case is O(n))

import unicodedata
from collections import Counter
class Solution:
    def IsAnagram(self, s: str, t: str) -> bool:
        # normalize s and t
        s = unicodedata.normalize("NFC", s)
        t = unicodedata.normalize("NFC", t)
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)
    
# Time: O(n)
# Space: O(n)



