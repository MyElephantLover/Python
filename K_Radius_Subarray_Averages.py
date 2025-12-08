# You are given a 0-indexed array nums of n integers, and an integer k.
# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
# The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.
# For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

# Constraints:
# n == nums.length
# 1 <= n <= 105
# 0 <= nums[i], k <= 105

class Solution:
    def RadiusSubArray(self, nums: List[int], k: int) -> List[int]:
        # boundary check
        # if there is only one element is considered, the average would be the element itself
        if k == 0:
            return nums 
        
        # initialize variables
        window_size = 2 * k - 1
        n = len(nums)
        averages = [-1] * n # if all index are invalid, the average would be all -1
        
        if window_size > n:
            return averages # if less than k indices on the left or right, return averages with all -1

        # generate prefix sum array
        # prefix[i + 1] would be the sum nums[0] to nums[i]
        prefix = [0] * (n + 1)
        for i in range(n): # from index 0 to n - 1
            prefix[i + 1] = prefix[i] + nums[i]

        # we iterate over only those indices with their left and right bound with at least k elements
        for i in range(k, n - k):
            leftBound, rightBound = i - k, i + k
            subArraySum = prefix[rightBound + 1] - prefix[leftBound]
            average = subArraySum // window_size
            averages[i] = average

        return averages

# Time Complexity: O(n) where n is the length of the array nums. Initializing the averages array with -1 takes O(n) time. And we iterate over
# the entire array to find the k-radius average with each index, which takes O(n) time
# Space Complexity: O(1)