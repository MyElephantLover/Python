# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def containDuplicates(self, nums: List[int]) -> bool:
        # initialize a hashmap to store {value: freq} pairs

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1 # increment by 1 if seeing the same value more than once

        for i, cnt in freq.items():
            if cnt >= 2:
                return True
            
        return False # if none of the return happened before, return False
    
# Time Complexity: O(n) as membership lookup in a dic takes on average O(1) and we iterate over
# the array once to build the dic

# Space Complexity: O(n) for the dic can store up to the length of n unique value in the array nums


# -- faster and less complex soultion -- #

class Solution:
    def containDuplicates(self, nums: List[int]) -> bool:
        # use a set, no need to store counts

        seen = set()

        for num in nums:
            if num in seen: # here seen is an empty set
                return True
            seen.add(num) # we add to seen after checking. if we did this earlier, the first occurance would not be added and duplicates not bee detected
        return False

# Time Complexity: O(n)
# Space Complexity: O(n) for the maximum distinct value in nums is n