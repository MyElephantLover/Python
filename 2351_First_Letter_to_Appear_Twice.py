# Given a string s consisting of lowercase English letters, 
# return the first letter to appear twice.

# Note:

# A letter a appears twice before another letter b if the second occurrence of a is 
# before the second occurrence of b.
# s will contain at least one letter that appears twice.

# Constraints:

# 2 <= s.length <= 100
# s consists of lowercase English letters.
# s has at least one repeated letter.

class Solution:
    def lettersTwice(self, s: str) -> str:
        seen = set() # a set is perfect here for: 1) stores unique values 2) membership check takes an average O(1) time

        for c in s:
                if c in seen:
                     return c
                # add c to the set
                seen.add(c)

# Time Complexity: O(1)
# Space Complexity: O(n) the set space grows linearly with the input size



