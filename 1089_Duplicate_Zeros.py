# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9

class Solution:
    def duplicates(self, arr: List[int]) -> None:
        # We could use backward two-pointer approach for this
        # The reason why we do not use forward two-pointer is that
        # we would overwirte the values not yet read with the duplicated zeros
        # hence, we read the elements from the left, but copy write from the right
        # we also need to handle the edge case when the arr[i] is at the exact boundary
        # that we do not duplicate zeros

        # initialize variables
        n = len(arr)
        zeros = 0 # the number of elements inserted before this index
        end = n - 1 # this is the last index in the original array that can fit the new array

        # Step 1: count zeros

        i = 0 # Think of i as reader pointer
        while i <= end - zeros: # after duplication of zeros, how many elements / indices left
            if arr[i] == 0:
                if i == end - zeros: # if after duplicates, arr[i] is at the boundary
                    arr[end] == 0 # we filled the last element as 0
                    end -= 1 # reduce the shift
                    break # immediately end the loop
                zeros += 1 # if not at the boundary, increment zeros by 1
            i += 1 # increment reader pointer

        # Step 2: Copy backwards
        last = end - zeros # the remaining spaces / indices
        for i in range(last, -1, -1): # loop from the last index backwards
            if arr[i] == 0:
                arr[i + zeros] = 0 # zeros mean the current final position
                zeros -= 1
                arr[i + zeros] = 0 # we write 0 twice
            else:
                arr[i + zeros] = arr[i] # not duplicate zeros

# Time Complexity: O(n) where n is the length of the array. We do two passes on the array
# The one is to find the duplicates(zeros), and the other one is to copy backwards
# In the worst case, there is less or no zeros and we need to go through every element
# Space Complexity: O(1)










        # Step 2: Copy elements backwards
