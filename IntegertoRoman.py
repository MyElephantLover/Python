class Solution:
    def romanInteger(self, num:int) -> str:
## define a list of tuples to store the mapping of roman numerals to integers
        dic = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

# define an empty list to store the roman numerals

        roman_digits = []

        for value, symbol in dic:
# we do not want to continue looping through it if num reaches the end
            if num == 0:
                break
# otherwise
            count, num = divmod(num, value) 
        # the divmod() function takes two numbers and return the tuple of its quotient and remainders when doing
        # integer division
        # append "count" copies of symbol to roman_digits
            roman_digits.append(symbol * count)

        return "".join(roman_digits) # "".join() is a string method used to concatenate a list or any interables
    # of strings into a single string

# Time Complexity: O(1)
# Space Complexity: O(1)

# In Python, this is a dic = {"M": 1000, "C": 100}
# This is a list of tuples - dic = [(1000, "M"), (100, "C")]

        


