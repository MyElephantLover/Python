# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

# Use two pointers and an extra res array

class Solution:
    def merge_Sort(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer1 = m - 1
        pointer2 = n - 1
        writer_idx = m + n - 1 # writer pointer

        # nums2 is the array that needs to exhaust, hence, we loop through nums2 and compare with nums1
        # we copy backwards from bigger numbers to the smaller numbers

        while pointer2 >= 0: # meaning n >=1
            if pointer1 >= 0 and nums1[pointer1] >= nums2[pointer2]: # when copying backwards, we always write the bigger element to the rightmost 
                # available position first, and the smaller value would naturally be placed to the front because:
                # 1) largest numbers been pulled out first that creates space at the front to be overwritten safely, and res decrements by 1 
                # if we are allowed to create another array, res, that would be the 0's at the front
                nums1[writer_idx] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[writer_idx] = nums2[pointer2]
                pointer2 -= 1
            writer_idx -= 1

# Time Complexity: O(m + n) the while loop traverse at most (m + n) times; we traverse each array once
# Space Complexity: O(1) since we modify nums1 in-place and did not create extra data structure



    

