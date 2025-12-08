# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# Constraints:
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100

class Solution:
    def minValue(self, nums: List[int]) -> int:
        # never less than 1 means >= 1
        # we could set the startValue to be 1
        # since the step-by-step sum needs to be >= 1, we set "total" and "min_val" as 0
        # where total is the current total, and min_val is the step-by-step sum

        startValue = 1
        total = 0
        min_val = 0

        for num in nums:
            total += num
            min_val = min(total, min_val)

        return -min_val + 1 # because the minimum value of startValue is -min_val + 1, because if startValue is 0, min_val + startValue > = 1, startValue = -min_val + 1
    
# Time Complexity: O(n) where n is the length of nums - we only iterate the array once
# Space Complexity: O(1) we just need to calculate the step-by-step total and the minimum value of the step-by-step total. Both requires constant space


