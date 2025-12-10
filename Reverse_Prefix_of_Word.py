# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

## The first approach is to use stack - stack is first in last out, so when we pop elements from a stack
## the order is reversed

## two things to do:
## Firstly, find the index for ch; secondly, reverse the prefix from the index of ch if found; if not found, return word

## initialize variables

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
    stack = []
    index = 0 # the index of ch
    result = [] # store the result set

    while index < len(word):
        stack.append(word[index]) # fill out the stack
        if word[index] == ch: # found ch
            while stack: # loop until the stack becomes empty
                result.append(stack.pop()) # pop() remove the element from word, and append to the result
            index += 1 # otherwise, continue

        # fill out the rest of the result set with the characters after the index
            while index < len(word): # this corresponds to the block #23
                result.append(word[index])
                index += 1 # index needs to continue increments until index reaches to the end of the string
            return "".join(result) # match the block #22
        
        index += 1 # meet with the outer while loop #20

    return word # if none of the previous return happend, return word


# Two pointer approach #

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # use left and right pointers to swap orders
        left = 0
        # create a result set with original order
        result = list(word)

        for right in range(len(word)): # from index 0 to index len(word) - 1
            # we found ch - swap characters from index 0 to the index of ch
            # we modify the result set directly
            if result[right] == ch:
                while left < right:
                    result[right], result[left] = result[left], result[right] # becasue result[right] is the index for ch, which needs to be reversed to index 0
                    left += 1
                    right -= 1
                return "".join(result)
            
        return word # this block is unindented means it only execute after the whole loop finished and never found a match with ch
    
    # Time Complexity: O(n) for both stack and two-pointer approaches
    # Space Complexity: O(n) as we create stack which grows up to n elements and in two pointers we create a result list which contains
    # n elements





