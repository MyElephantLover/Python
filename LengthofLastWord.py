class Solution:
    def lengthLastWord(self, s: str) -> int:

        # First, we need to consider some edge cases - 
        # 1) the str is 0
        # 2) there are trailing spaces in the input string
        # 3) there might only be one word in the given string

        # Secondly, we try to locate the last word, starting from the end of the string
        # iterate through the string in reverse order, consuming the empty space
        # when we first come across a non-space character, we know we are at the last character of the last word

        # Thirdly, once we locate the last word, we count its length, starting from its last character, we could
        # use a loop here

        # trim the trailing spaces
        p = len(s) - 1 # p being the index of the last character
        while p >= 0 and s[p] == " ": # p >= 0 meaning len(s) >= 1
            p -= 1 # each time through the loop, we move one character to the left

        # compute the length of the last word
        length = 0
        while p >= 0 and s[p] != " ":
            p -= 1
            length += 1

        return length
    
# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(1) only constant memory is consumed, regardless of the input string