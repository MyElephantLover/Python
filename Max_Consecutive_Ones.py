# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# The logic is similar to two pointers. 
# we use counter as the current counter which increment by 1 when we encounter 1
# max_counter is the maximum consecutive 1's until now
# we update max_counter when counter moves along. 
# when encoutering 0, we reset counter to 0

class Solution:
    def maxConsecutive(self, nums: List[int]) -> int:
        # initialize variables
        counter = 0
        max_counter = 0

        for num in nums:
            if num == 1:
                counter += 1
                max_counter = max(max_counter, counter)
            # encouter 0
            # reset counter to 0
            counter = 0
        return max(max_counter, counter)
    
# Time Complexity: O(n) we traverse the array once 
# Space Complexity: O(1)
    
# One-Line Solution from others
class Solution:
    def consecutive(self, nums: List[int]) -> int:
        return max(len(''.join(map(str, nums)).split('0')))
    
# .split() is a string method, and string contains characters; .split() breaks
# a string into substrings based on defined separator (character)
# map applies functions to all elements in the iterable
# len is a function to return the length of a single object

    


