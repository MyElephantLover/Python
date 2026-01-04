# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# # You can return the answer in any order.

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # use a hash map to store {value: index}
        seen = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment], i]
            seen[num] = i # otherwise, add num to seen and its corresponding index

# Time Complexity: O(n) one-pass
# Space Complexity: O(n) as the maximum key stored in the hashmap is n
