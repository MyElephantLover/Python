# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

# being sorted non-descending order means when reading an array from left to right
# elements are not descending

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # we use two pointers, reader and writer to traverse the array
        # when there is a duplicate, for sorted array, they stay side by side
        # hence, when reader pointer reaches unique next element, writer pointer write the element
        # otherwise, writer pointer does not move; reader pointer would continue move forward
        # we start at the index 1 since index 0 is always the unique value seeing for the first time

        writer = 1

        for reader in range(1, len(nums)):
            if nums[reader] != nums[reader - 1]: # the next element is unique
                nums[writer] = nums[reader] # writer pointer write down the element
                writer += 1 # writer pointer move on
        return writer

    # Time Complexity: O(n) as we only traverse the array once
    # Space Complexity: O(1) we modify the array in-place
    
     