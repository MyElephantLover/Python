# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.

class Solution:
    def maxNumberofBalloon(self, text: str) -> int:

        # the hint askes us to count the letter: freq in string

        freq = {}

        for ch in text: # string is already an iterable, no need to convert it to a list
            freq[ch] = freq.get(ch, 0) + 1 # add key:value to the dictionary

        # balloon: 'a':1 , 'b': 1, 'l': 2, 'o': 2, 'n': 1

        return min(
            freq.get('a', 0),
            freq.get('b', 0),
            freq.get('l', 0) // 2,
            freq.get('o', 0) // 2,
            freq.get('n', 0)
        ) # the key is to find the scarcest resource in "balloon", which is the minimum of letters
        # we need to form a complete 'balloon'

    # Time Complexity: O(n) to build the hashmap, and scan the whole string
    # Space Compelxity: O(1) for the hashmap can store at most 26 lowercase English letters

