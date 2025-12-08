# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

class Solution:
    def maxAverage(self, nums:List[int], k: int) -> float:
        # initialize a current value as 0

        curr = 0
        for i in range(k): # from the index 0 to the index k - 1
            curr += nums[i] # curr is the sum of the contiguous subarray with the length of k

        ans = curr

        # we also need to check the subarray from the index k - 1 to the end of the array nums
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k] # we add the new element nums[i] to the window and remove the element nums[i - k]
            ans = max(ans, curr) # because ans has been assigned as curr in the previous loop, and this step means ans compares with all the loops

        return ans / k
    
# Time Complexity: O(n) where n is the length of the array, nums
# Space Complexity: O(1)