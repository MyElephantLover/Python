class Solution:
    def minSubArrayLen(self, target:int, nums:List[int]) -> int:
        # my instinct is to use two pointers
        # later I learned that in this problem, we use sliding windows
        # the key concept to bear in mind is: Only if the length of the current subarray
        # is smaller to target should we append the elements to the subarray.
        # when the subarray is larger or equal to target, we will attempt to update our answer
        # with the length of the current subarray

        # to "add" elements to the window, we loop over the array by incrementing right
        # if the sum of the array exceeds or equal to target, we reduce the elements by incrementing left

        left = right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]
             # we iterate over the window starting right from right = 0 to right = len(nums) - 1
            while sumOfCurrentWindow >= target: # we reduce elements by incrementing left
                sumOfCurrentWindow -= nums[left]
                left += 1
        return res if res != float('inf') else 0 # if no such subarray returns 0
    
# Time Complexity: O(n) where n is the length of nums, threre is a while loop inside a for loop, but the inner loop 
# is not running n times for each iteration of the outer loop. A sliding window guarantees a maximum of 2n window
# iterations
# Space Complexity: O(1) we are not using extra space except for some integer variables which take up constant
# space each



