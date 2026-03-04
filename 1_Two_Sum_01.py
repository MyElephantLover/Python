# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # set up a hash map to store number -> index 
        seen = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment], i] # seen[compliment] is the index of the number value from nums, i is the index of the current value
                # [index_of_compliment, index_of_curr_value]
            else:
                seen[num] = i

# Time: O(n) as we store the value and check if the compliment exists, each loop is O(n); if we check each pair, it would be O(n^2)
# Space: O(n) because the dictionary can grow up to n elements
