# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# -- Intution --
# Treat value 0 as -1, value 1 is 1
# hence when the sum of the subarray equals 0, there's a balanced number of 0 and 1
# the longest length in the subarray is the index - first_seen[prefix_sum]

from typing import List

class Solution:
    def fineMaxLength(self, nums: List[int]) -> int:
        # initialize first seen as a dic
        first_seen = {0: -1} # key: prefix_sum; value: index it was first seen 
        prefix_sum = 0
        best = 0

        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1

            if prefix_sum in first_seen: # is prefix_sum a key in the dictionary
                best = max(best, i - first_seen[prefix_sum])
            else:
                first_seen[prefix_sum] = i

        return best 

# Time Complexity: O(n) dictionary lookup takes O(1) and we iterate over the array once
# Space Complexity: O(n) the dictionary can store up to (2n + 1) sums 

