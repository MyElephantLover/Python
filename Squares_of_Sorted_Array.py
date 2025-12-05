# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order. 

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

class Solution:
    def Squares_Sorted_array(self, nums:List[int]) -> List[int]:
        # initiate an array res to store the result
        res = []
        for i in range(0, len(nums)):
            res[i] = nums[i] * nums[i]
        return sorted(res)

# Time Complexity: O(nlogn), because squares takes O(n) and sorting takes O(logn) where n is the length of nums
# Space Complexity: O(n) or O(logn)    

# Because the array is sorted, we can use two-pointers to reduce time complexity by only going through the array once
# When the abs(L) > abs(R) that means the SQR(L) > SQR(R), becasue if nums[L] is negative, its squared value would become positive
# we can use two-pointers to reduce the time complexity to O(n)

class Solution:
    def Squares_Sorted(self, nums:List[int]) -> List[int]:
        # initialize two pointers, left and right
        n = len(nums)
        left = 0
        right = n - 1

        # initialize an array res to store the result
        res = [0] * n

        for i in range(n - 1, -1, -1): # iterate i backwards from n - 1 to 0, inclusively
            if abs(nums[left]) < abs(nums[right]): # place the squares of the right pointer
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            res[i] = square * square
        return res

# Time Complexity: O(n), as we only iterate over the array nums once
# Space Complexity: O(n) if we take output into account; otherwise, O(1)