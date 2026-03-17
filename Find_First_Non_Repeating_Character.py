# Problem:
#  "swiss" → "w"

class Solution:
    def firstUnique(self, s:str) -> str:

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in s:
            if count[ch] == 1:
                return ch
            
        return None

# Time: O(n) for n is the number of characters in the string
# Space: O(n) in the worst case, all characters are unique and added to the hash map





