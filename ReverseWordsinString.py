class Solution:
    def reverseWords(self, strs: str) -> str:
        return " ".join(reversed(strs.split())) # what this line of code is doing, is it removes extra
    # whitespaces from the string strs, including leading and trailing spaces and multiple whitespaces
    # between words, and return a cleaned-up version of the string with single spaces between words
 