# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Constraints:

# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
 
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

class Solution:
    def missingNum(self, nums: List[int]) -> int:
        n = len(nums)

        # Use the math formula sum(0...n) = n*(n + 1) // 2

        return n*(n + 1) // 2 - sum(nums)
    
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def missingNum(self, nums: List[int]) -> int:
        n = len(nums)
        Set = set(nums) # store unique values in nums

        for i in range(0, n + 1): # problem states the range is [0, n]
            if i not in Set:
                return i 
            
# Time Complexity: O(n) Python checks each value in nums to add it to the Set
# Space Complexity: O(n) the Set takes extra space