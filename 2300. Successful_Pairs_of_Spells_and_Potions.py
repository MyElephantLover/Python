# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

# Constraints:

# n == spells.length
# m == potions.length
# 1 <= n, m <= 105
# 1 <= spells[i], potions[i] <= 105
# 1 <= success <= 1010

# Idea: for each spell, we want to know how many postions p satisfy (s * p >= success) => p >= success / s

from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        pairs = []

        for spell in spells:
            left = 0
            right = m - 1
            first_valid = m # default: no valid postion
            # all indices from first_valid onward are valid

            while left <= right:
                mid = (left + right) // 2

                if spell * potions[mid] >= success:
                    first_valid = mid
                    right = mid - 1
                else:
                    left = mid + 1

            pairs.append(m - first_valid) # because the array is sorted, we use total_length - start_index
        
        return pairs
    
# Time: O(mlogm + nlogn) where m is the length of postions and n is the length of spells
# we did binary search for each spell
# Space: O(1)
