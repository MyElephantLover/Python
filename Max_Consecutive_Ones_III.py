# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        read = 0
        zeros = 0 # used to track zeros counts
        best = 0 # the best at the current iteration

        for write in range(len(nums)): # you can use while, but need to remember increment at the end
            if nums[write] == 0:
                zeros += 1

            while zeros > k: # the window becomes invalid
                if nums[read] == 0: # read only moves when window becomes invalid, to remove elements from the left
                    zeros -= 1
                read += 1 # read moves forward

            best = max(best, write - read + 1) # the size of the current valid window is write - read + 1
            # it has to be insdie the write pointer loop, as each iteration changes the window (each time write moves)

        return best

## we use for loop for write because it moves in a fixed, predictable way, one step at a time
## the read pointer moves in a conditional, variable way, only when the window is invalid

# Time Complexity: O(n) for write pointer visits every value once
# Space Complexity: O(1)