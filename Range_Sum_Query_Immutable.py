# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= left <= right < nums.length
# At most 104 calls will be made to sumRange.

## Brute Force Approach

class NumArray: # class means this is our tool to create an object, meaning we are creating our own data structure
    def __init__(self, nums: List[int]): # In python, __init__runs when objects are created
        self.nums = nums # self here means "this object instance" which can be reused between method calls

    def rangeSum(self, left: int, right: int) -> int:
        total = 0

        for i in range(left, right + 1): # this loop has (right - left + 1) elements
            total += self.nums[i]

        return total

# Time Complexity: O(n) because in worst-case scenario, this can be as wide as the entire array
# Space Complexity: O(1)

## Prefix Sum Approach

class NumArray:
    def __init__(self, nums: List[int]):
        # create prefix sum here with O(n) time
        self.prefix = [0] # Python list is dynamic so grows automatically with elements appended
        running_sum = 0

        for num in nums:
            running_sum += num
            self.prefix.append(running_sum)

    def rangeSum(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
    
# Time Complexity: O(n) we traverse the whole array nums with length n
# Space Complexity: O(1)


