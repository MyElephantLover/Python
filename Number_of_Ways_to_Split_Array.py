class Solution:
    def valid_Splits(self, nums:List[int])-> int:
        n = len(nums)

        # initialize prefix sum array
        prefix = [0]*n
        prefix[0] = nums[0]

        for i in range(1, n): # skips the first index as 0 - 1 would be negative
            prefix[i] = prefix[i - 1] + nums[i]

        for i in range(n - 1): # split the left and right sections from 0 to n - 2
            left_section = prefix[i]
            right_section = prefix[n - 1] - prefix[i]
            if left_section >= right_section:
                ans += 1
        return ans
    
# Time Complexity: O(n)
# Space Complexity: O(1)

# We can set left_section to 0 to reduce the need to set an array to improve the time complexity
# becasue left_section increases incrementally as i increments with 1 iteration

class Solution:
    def split_Array(self, nums:List[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums)- 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1
        return ans
    
# Time Complexity: O(1)
# Space Complexity: O(1)