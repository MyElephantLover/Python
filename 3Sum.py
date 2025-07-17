class Solution:
    def twoSum(self, nums: List[int]) -> List[List[int]]:
        # return a list of tuples

        # This approach uses Two Pointers
        # what I missed in the beginning is to sort the array
        # after sorting, the two indices, i, j, and k's bounds become clear
        res = []
        nums.sort()

        for i in range(len(nums)):
            # look at edge cases
            if nums[i] > 0:
                break # break early if the current number is positive
            # because in a sorted array, if nums[i] > 0, then any two numbers
            # after it will also be positive and can't sum to zero

            if nums[i] == 0 or nums[i] != nums[i - 1]: # advoid duplicates
                self.twoSumII(nums, i, res)
        return res
    
    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1 # move the lower end to the right
            elif sum > 0:
                hi -= 1 # move the upper end to the left
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]: # if there're duplicates
                    lo += 1 # move the lower pointer to the right

# Time Complexity: O(n^2) where n is the length of nums, since we have two while loops
# Space Complexity: from O(logn) to O(n) depending on the implementation of the sorting algorithm

            


