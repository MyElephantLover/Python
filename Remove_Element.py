# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.


class Solution:
    def removeElement(self, nums: List[int], val:int) -> int:
        # we use two pointers to traverse the array from the front and the back
        # define variables
        n = len(nums)
        end = n - 1 # this is the last element we can still check, aka, within the valid (unchecked) range

        i = 0 # i loop from left to right, end checks backwards
        while i <= end: # because end is shrinking, elements after end is not important
            if nums[i] == val:
                nums[i] = nums[end] # overwrite current value with the last unchecked element
                end -= 1 # shrink the window to the left
            else:
                i += 1 # meaning nums[i] != val, keep it and i moves forward

        # After the loop, indices [0...end] contains the elements non-val
        return end + 1 # plus the index 0
    
# Time Complexity: O(n) as the while loop traverses the array once, i moves forward, end moves backwards; though there are swaps, the number
# of operations remain linear
# Space Complexity: O(1) as we change nums in-place
