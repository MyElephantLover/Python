# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        seen = {} # stores a mapping in a dictionary, in Python, a dictionary is a hash table

        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            else:
                seen[num] = i # add un-seen pair to the dictionary

# Time Complexity: O(n) as we traverse the dictionary / hash table once to look for match with num; Python use hash table to use
# a hash fucntion to get to an average of O(1) time for insert, lookup and fetch
# Space Complexity: O(n) as the memory the hash table uses would scale linearly with the input size

# Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)): # i takes value from 0 to n - 1
            for j in range(i + 1, len(nums)): # j takes value from i + 1 to n - 1
                if nums[i] + nums[j] == target:
                    return [i, j]
                
# Time Complexity: O(n^2) as we have two for loops
# Space Complexity: O(1)