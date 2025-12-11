# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

# Constraints:

# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

# we understand the pivot index is the index i where the sum from index 0 to index i - 1
# the same as the sum from index i + 1 to index n - 1 when n is the length of the array
# we can look at this in simplier way where the right sum is the total sum - leftSum - nums[i]
# this would take O(n)

class Solution:
    def(self, nums: List[int]) -> int:

        # initialize variables
        S = sum(nums)
        leftSum = 0
    
        for i, x in enumerate(nums): # using enumerate extract pairs of index and the corresponding value in a list
            # enumerate() does not create a new list, it just create an interator that yield (i, x) pairs on the fly
            # each step takes O(1). You can call it once per element, so total is O(n)
            if leftSum == S - leftSum - x: # means left = right
                return i
            leftSum += x # otherwise, adding the value to the right to leftSum
        return -1 # if previous return did not happen, return -1

# Time Complexity: O(n) since we only traverse the array once to calcuate the sum, S.
# Space Complexity: O(1) we did not allocate extra memory