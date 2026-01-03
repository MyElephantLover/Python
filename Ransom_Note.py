# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

class Solution:
    def ransomNote(self, ransomNote: str, magazine: str) -> bool:
        # initialize a hashmap / dictionary to store the letters and their respective counts in magazine
        freq = {}

        for ch in magazine: # a string is an iterable, so we can directly iterate over it to get letters
            freq[ch] = freq.get(ch, 0) + 1 # if ch is a new key, default count is 0, otherwise, increment by 1

        for ch in ransomNote:
            if freq.get(ch, 0) == 0: # meaning ch is not in freq, or has been used up
                return False 
            freq[ch] -= 1 # otherwise, ch has seen in magazine, decrement by 1 to prevent reuse
        return True # if none of the return happened, return True
    
# Time Complexity: O(n + m) dictionary membership lookup takes on average O(1), we runs once for each ch in magazine and ransomNote
# Space Complexity: O(1) the maximum key in the dictionary is 26 lowercase eng letters 