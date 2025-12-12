# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109

class Solution:
    def largest(self, nums: List[int]) -> str:
        # convert each element in the list into string
        nums_s = [str(num) for num in nums]

        # sort the list in descending order

        nums_s.sort(key = lambda x: x * 10, reverse = True) # "*" here means string repetition, not numeric multiplication
        # by default, sort() is ascending, so reverse = True means we sort in descending order

        # heandle if the leftmost digit is 0
        if nums_s[0] == "0": # because string contains characters and here the list has been sorted
            return "0" # because the question ask to return a string
    
        return ''.join(nums_s)
    
# Time Complexity: O(nlogn), sorting takes O(nlongn)
# Space Complexity: O(n + S) depends on language, space complexity can range
# from O(n) to O(logn)

