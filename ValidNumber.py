class Solution:
    def isNumber(self, s:str) -> bool:
        # define the three variables seen_digit, seen_exponent and seen_dot
        seen_digit = seen_exponent = seen_dot = False

        for i, c in enumerate(s): # enumerate() loops over a list or tutple
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]: # sign
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E": # the last character is not an exponent
                    return False
            elif c in ["e", "E"]: # exponent
                if seen_exponent or not seen_digit: # exponent without digits is not a valid number
                    return False
                # otherwise
                seen_exponent = True
                seen_digit = False
            elif c == ".": # dot
                if seen_dot and not seen_exponent: # cannot be valid number with only dots or exponents
                    return False
                seen_dot = True
            else:
                return False
        return seen_digit

## Time Complexity: O(N) where N is the length of s
## Space Complexity: O(1), we only store the three variables, seen_digit, seen_dot and seen_exponent

