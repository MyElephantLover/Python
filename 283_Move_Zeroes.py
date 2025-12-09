# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 
# Follow up: Could you minimize the total number of operations done?

class Solution:
    def moveZero(self, nums: List[int]) -> None:
        # from the constraint, we can see the length of nums is >= 1

        # we use two pointers to traverse the array separately, the reader pointer to go through every element
        # while the writer pointer only writes when the element the reader pointer is on is not 0

        # initialize variable
        writer = 0

        for reader in range(len(nums)):
            if nums[reader] != 0:
                # writer pointer writes it down
                nums[writer] = nums[reader]
                writer += 1

        # now we need to fill out the rest of the array with 0's
        while writer < len(nums):
            nums[writer] = 0
            writer += 1

# Time Complexity: O(n) each loops traverse the entire array of length n
# Space Complexity: O(1) we did this in-place

## Follow up ##
# we can reduce unnecessary writes when only reader is not the same as writer, meaning reader is 0 
# we can swap the reader and writer so the position remaining would natually fill in with 0
# because when reader not the same as writer, reader is 0

class Solution:
    def move(self, nums: List[int]) -> None:
        writer = 0
        for reader in range(len(nums)):
            if nums[reader] != 0:
                if reader != writer:
                    nums[writer], nums[reader] = nums[reader], nums[writer]
                writer += 1

# Time Complexity: O(n) 
# Space Complexity: O(1)