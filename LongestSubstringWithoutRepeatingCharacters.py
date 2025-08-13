from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        ## my intuition is to use two pointers - left and right
        ## from previous other problems - compare the adjacent characters
        ## if the characters are duplicated, move to the next position
        
        chars = Counter()

        left = right = 0 # define left and right pointers

        res = 0

        while right < len(s):
            r = s[right]
            chars[r] += 1 ## move to the next position

        while chars[r] > 1: ## valid, not run out of characters
            l = s[left]
            chars[l] -= 1 ## decreasing by left pointers
            left += 1

        res = max(res, right - left + 1) ## update res
        right += 1
    
        return res

## Time Complexity: O(n), the worst case is O(2n) that each character is reached twice by 
## left and right

## Space Complexity: O(min(m, n)), we need O(k) for the sliding window, where k is the size
## of the Set. The size of the Set is upper bounded by the size of the string n and the 
## size of the alphabet / charset m.



