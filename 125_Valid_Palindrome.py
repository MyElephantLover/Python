# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # the best practice is to use two pointers
        # we convert the string to lowercase, ignore non-alphanumetric characters

        left = 0
        right = len(s) - 1

        while left < right:
            # skip non-alphanumetrc from the left
            while left < right and s[left].isalnum():
                left += 1 # left moves forward to the right

            # skip non-alphanumeric from the right
            while left < right and s[right].isalnum():
                right -= 1 # right moves to the left

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True # if none of the return happened, return True
    
# Time: O(n) we scan the string once
# Space: O(1) no extra string created


# Pythonic Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]
    
# Time: O(n)
# Space: O(n)


    

    


