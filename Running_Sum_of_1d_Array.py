# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Constraints:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

class Solution:
    def runningSumArray(self, nums: List[int]) -> List[int]:
        # define variables
        n = len(nums)
        # initialize a result list, runningSum
        runningSum = [0] * n # pre-allocate the array to make it the same size as the array, nums
        # fill the index 0 with the first value in the list, nums, since the first element is the first running sum
        runningSum[0] = nums[0]

        for i in range(1, n): # start from the index 1
            runningSum[i] = runningSum[i - 1] + nums[i]

        return runningSum
    
# Time Complexity: O(n) where n is the length of the list, nums. We traverse the whole list once
# Space Complexity: O(1) as we do not use additional memory proportionally to the input array 