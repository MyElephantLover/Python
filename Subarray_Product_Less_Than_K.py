# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106

class Solution:
    def subarray_product(self, nums:List[int], k: int) -> int:
        # use sliding window, the multiplication of the left and right pointers, 
        # to compare with the value of curr.
        # if the multiplicatino is less than curr, then the ans would increment by 1

        # because the constraint shows nums[i] >= 1 and k >= 0
        # which means any products would not be less than k if k <= 1
        if k <= 1:
            return 0
        
        # initialize ans and left pointer to be 0
        ans = left = 0
        curr = 1
        for right in range(0, len(nums)):
            curr *= nums[right]
            while curr >= k: # meaning the window needs to shrink to the left because we are looking for greater than k
                curr //= nums[left]
                left += 1 # left pointer moves to the right

            ans += right - left + 1
        
        return ans

# Time Complexity: O(n) where n is the length of nums. We iterate over the whole array
# Space Complexity: O(1) these variables, left, right, ans do not depend on the size of the input array




