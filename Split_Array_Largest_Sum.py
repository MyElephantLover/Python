# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= k <= min(50, nums.length)

# Idea: split nums into k subarray to make the largest subarray sum minimized
# so binary search on: 
# 1) smallest possible answer: max(nums) because no subarray can have sum smaller than the biggest single element
# 2) larget possible answer: sum(nums) one subarray containing everything is always possible
# for a guess value mid, ask: can I split nums into k sbarrays that each subarray have sum <= mid?

class Solution:
    def splitArrayLargestSum(self, nums: List[int], k: int) -> int:
        def can_split(max_sum: int) -> bool:
            subarrays = 1 # before spliting, we already have one subarray
            curr_sum = 0

            for num in nums: # can I add this number to the curr subarray so it will not exceed the max_sum?
                if curr_sum + num > max_sum:
                    subarrays += 1
                    curr_sum = num # the number becomes the first element of the new subarray
                else:
                    curr_sum += num

            return subarrays <= k # if minimum required is <= k, we can adjust to exactly k
        
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2
            if can_split(mid): # subarrays <= mid
                right = mid - 1 # if mid works, we search left side to see if we can find a little smaller
            else: # if mid fails, meaning mid is too small, need to move left to the right; large mid is always valid
                left = mid + 1

        return left

# Time: O(n log S) where S is the sum of nums; each binary search step is O(n), for num in nums, and we do it O(logS) times
# Space: O(1)
