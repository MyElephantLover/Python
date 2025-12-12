# Given an array nums of integers, return how many of them contain an even number of digits.

# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 105

class Solution:
    def evenDigits(self, nums: List[int]) -> int:
        # since string is easier for calculating digits
        # let's convert every element to a string
        # and we can use len() function to calculate the length

        count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
    
# Time Complexity: O(nlogm) where n is the length of nums and m is the maximum
# integer in the array
# Space Complexity: O(logm) we temporarily store a string of length m for num 