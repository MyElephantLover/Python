# You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

# You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

# Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

# Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

# Constraints:

# 0 <= k < sweetness.length <= 104
# 1 <= sweetness[i] <= 105

# The goal is to maximize the minimum sweetness among (k + 1) groups

# Key idea: suppose you guess that your piece can have at least x sweetness,
# can you cut the chocolate into at least k + 1 pieces such that every piece has a total sweetness >= x
# we can check this greedily by
# 1) walk through the array
# 2) keep adding chucks
# 3) whenever the running sum reaches x, cut there and start a new piece
# if you can make at least (k + 1) pieces, then x is feasible
# so use binary search to find the largest feasible x

from typing import List
class Solution:
    def divideChocolate(self, sweetness: List[int], k: int) -> int:
        def can_make(target: int) -> bool:
            pieces = 0
            curr_sum = 0

            for s in sweetness:
                curr_sum += s
                if curr_sum >= target:
                    pieces += 1 # cut here ad start a new piece
                    curr_sum = 0

            return pieces >= k + 1
        
        left = 1
        right = sum(sweetness) // k + 1 # the maximum possible sweetness (total >= x+x+...) = x * (k + 1)
        # because we are searching for the maxmimum valid minimum piece 

        while left <= right:
            mid = (left + right) // 2

            if can_make(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right # when the while look ends, left <= right, so left lands on the first invalid value; right lands on the last valid value
        # we are looking for the maximum valid minimum value

# Time: O(nlogS) where n is the length of sweetness and S is the sum of sweetness
# binary search range is from 1 to sum(sweetness) // (k + 1)
# Space: O(1)
