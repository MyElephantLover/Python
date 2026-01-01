# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

# Constraints:

# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 1000

from typing import List

class Solution:
    def largestUnique(self, nums: List[int]) -> int:

        # count value and frequency - the intuition is hashmap

        freq = {}

        # count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 # freq.get(num, 0) is when the key does not exist

        # iterate over dictionary
        unique_nums = [num for num, count in freq.items() if count == 1]

        return max(unique_nums) if unique_nums else -1
    
# Time Complexity: O(n) for iterating over nums once, O(n) to build the freq map, O(n) to scan it
# Space Complexity: O(n) for the dictionary can store up to n keys