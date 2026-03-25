# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# The test cases are generated so that there will be an answer.

# Constraints:

# 1 <= nums.length <= 5 * 104
# 1 <= nums[i] <= 106
# nums.length <= threshold <= 106

# Idea: for a given divisor d, compute: 
# total = sum(ceil(num / d) for num in nums)
# we want the smallest divisor that works

from typing import List
class Solution:
    def findSmallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums) # left starts as 1 because divisor must be a positive integer
        # smallest possible divisor is 1

        while left < right:
            mid = (left + right) // 2
            total = 0

            for num in nums:
                total += (num + mid - 1) // mid # integer vision of ceil(num / mid)
                # left, right and mid are all postive divisor values

            if total <= threshold:
                right = mid # keep mid, and search left for smaller divisors
            else:
                left = mid + 1

        return left
    
# Time: O(nlogm) where n is the length of nums, m = max(nums) as binary search runs on the divisor range, not the array
# search space is [1, max(nums)] -> size: m
# Space: O(1) we only create a few variables

