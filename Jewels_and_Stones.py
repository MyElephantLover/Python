# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Constraints:

# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # The hint is, for each stone, check if it's a jewel

        # initialize a set to store unique jewels
        jewel_set = set(jewels)
        cnt = 0 # used to store how many stones are in jewel_set

        for stone in stones:
            if stone in jewel_set:
                cnt += 1

        return cnt
    
# -- Pythonic Solution -- #
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)

        return sum(stone in jewel_set for stone in stones)
    
# Time Complexity: O(n + m) where n is the length of the string jewels and m is the length of
# the string stones. Membership lookup takes on average O(1) and we iterate over each string once

# Space Complexity: O(n) where n is the length in the string jewels



