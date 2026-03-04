# Given an integer x, return true if x is a palindrome, and false otherwise.

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def Palindrome(self, x: int) -> bool:
        s = str(x)
        n = len(x)

        for i in range(0, n):
            if s[i] != s[n - i - 1]:
                return False
        return True
            
# Python one-liner

class Solution:
    def Palindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
    
# Time: O(n)
# Space: O(1)

# No String Conversion

class Solution:
    def Palindrome(self, x: int) -> bool:
        if x < 0: # handle negative number
            return False
        
        original = x # we will modify x during the loop, so we save the original value of x
        rev = 0 # this variable will store the reversed digits

        while x > 0: # we keep processing digits until no digits remain
            rev = rev*10 + x%10 # multiplying by 10 shifts digits to the left so we can add next digit to the end
            # rev*10 shift one place to the left, and + x%10 adds new digit at the end
            x //= 10 # remove the last digit

        return original == rev
    
# Time: O(log10n)
# Space: O(1) no matter how large x is, we still only store limited number of variables, so memory used does not grow with the input size



