# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


# sorted in non-descending order means duplicates sit next to each other
# we can use two pointers, reader and writer pointers, to reomve duplicates in-place
# we can use two approaches, the one is to check duplicates, and write the next element down
# the other one is to check unique values, and write down unique value

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

class Solution:
    def DuplicatesSorted(self, nums: List[int]) -> int:
        # initialize variables
        n = len(nums)
        writer = 1 # because the index 0 would always be unique

        if n == 0:
            return 0

        for reader in range(1, n): # because nums[0] is always the unique value
            if nums[reader] != nums[reader - 1]: # next index is unique value
                nums[writer] = nums[reader] # write the element down
                writer += 1 # only when there is unique value does writer increment by 1
        
        return writer
    
# Time Complexity: O(n) since the for loop traverses the array at most once where n is the length of the array
# Space Complexity: O(1) as we modify the array in-place


    


        