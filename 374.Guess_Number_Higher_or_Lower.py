# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# Constraints:

# 1 <= n <= 231 - 1
# 1 <= pick <= n

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1: # meaning guess / mid is higher than pick
                right = mid - 1
            else:
                left = mid + 1
            
# Time: O(log n) where n is the number of possible values for pick
# Space: O(1)                

