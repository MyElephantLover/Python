# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

from typing import List
class Solution:
    def searchInsertPosition(self, nums: List[int], target: int) -> int:
        # since it asks for the position if the target were not there, use left-closed, right-open interval
        # [left, right)

        left = 0
        
        while left < right: # we always end with left == right
            mid = (left + right) // 2
            # if nums[mid] == target: # don't have to explicitly check nums[mid] == target
            #     return mid # because if there is such index, we will land on it; otherwise,we will find the position it should have been inserted
            if nums[mid] < target: # I should search right side, so move left forward
                left = mid + 1
            else:
                right = mid # keep mid, could be answer

        return left # return right or left gives the same result, but we return left since it's the representation of the insert position by definition in this pattern

# Time: O(logn) where n is the length of the array - each iteration cuts the search space in half
# Space: O(1) we only created variables, left, right and mid
 
    

