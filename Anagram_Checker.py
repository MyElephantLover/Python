# Problem:
#  Check if two strings are anagrams.

# two strings are anagrams if they:
# 1) have the same characters
# 2) have the same frequency
# 3) the order does not matter

class Solution:
    def check_anagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False
        
        count = {} # use a hash map

        for ch in s: # first pass: we build counts with the first loop
            count[ch] = count.get(ch, 0) + 1

        for ch in t: # the reason why we used the same 'ch' because 'ch' just means the current character
            # we are looking at
            if ch not in count:
                return False
            count[ch] -= 1 # only runs if ch in s
            if count[ch] < 0: # this means we used more ch than it's available in s
                return False
            
        return True
    
# Time: O(n) for n is the length of the string
# Space: O(n) hash map worst case is all characters are unique
    

