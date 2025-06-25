class Solution:
    def RotateArray(self, nums:List[int], k:int) -> None:

        # This is brute force solution

        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                previous, nums[j] = nums[j], previous

# Time Complexity: O(n * k) because each steps shifted one step to the right for k times
# Space Complexity: O(1)
# Brute Force solution Exceeded Time Limit

# Another way is to create a new array

class Solution:
    def RotateArray(self, nums: List[int], k: int) -> None:

        n = len(nums)

        a = [0]*nums # define a as the new empty array. copied from nums

        for i in range(n):
            a[(i + k) % n] = nums[i]

        n[:] = a # This syntax means to replace the whole content of the list n with a

# Time Complexity: O(n) One pass is to put numbers to the new array, and another pass is to copy
# the new array to the original one 
# Space Complexity: O(n) we created a new array with the same size



