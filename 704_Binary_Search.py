# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# # You must write an algorithm with O(log n) runtime complexity.

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

# the problem states: "return -1 if index not found", we use closed interval version

from typing import List
class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 # inclusive

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else: # nums[mid] > target
                left = mid + 1

        return -1 # if none of the above happend, return -1
    
# Time: O(logn) where n is the size of the search space; each iteration cuts the search space in half
# Space: O(1) as we do not create extra data structure with the input data 