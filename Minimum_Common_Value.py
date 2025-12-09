# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

# Constraints:

# 1 <= nums1.length, nums2.length <= 105
# 1 <= nums1[i], nums2[j] <= 109
# Both nums1 and nums2 are sorted in non-decreasing order.

class Solution:
    minCommonValue(self, nums1: List[int], nums2:List[int]) -> int:
        # from constraints, we can see all alements in num1 and nums2 are >= 1
        # they are both sorted in non-descending order
        # hence, the first common integer found when iterating from left to right would be the minimum common value
        # we create a set which stores all distinct elements in nums1, and iterate through nums2 to see any common value

        set1 = set(nums1) # we store elements in nums1 into set1
    
        for num in nums2:
            if num in set1:
                return num # we found the minimum common value
            
        return -1 # this block executes after no previous return happened

# Time Complexity: O(m + n) where n is the length of nums1 and m is the length of nums2, creating set1
# iterate through all elements in nums1 and traverse every element in nums2
# Space Complexity: O(n) we initialize set1 which in worst case would be n distinct elements in nums1

## Two Pointers ##

class Solution:
    def minCommonTwo(self, nums1: List[int], nums2: List[int]) -> int:
        # initialize two pointers
        first = 0 # the poiter traverse nums1
        second = 0 # the pointer traverse nums2
        
        while first < len(nums1) and second < len(nums2):
            if nums1[first] < nums2[seond]: # meaning the element in nums1 is less
                first += 1
            elif nums1[first] > nums2[second]:
                second += 1
            else:
                return nums1[first] # we found the minimum common value

        return -1 # if none of the conditions met above, return -1

# Time Complexity: O(m + n) where m is the length of nums2 and n is the length of nums1. 
# Each pointer can iterate as many as (m + n) times. Each operation of the loop, we perform O(1) 
# Space Complexity: O(1) we use a couple of variables and no additional data structure that grows with 
# input size


## Binary Search ##
## Binary Search is a way to use O(logm) to look up a target in sorted arrays ##
## With BS, we use three pointers, left, mid and right to compare with the target

class Solution:
    def minCommonBinary(self, nums1:List[int], nums2:List[int]) -> int:
        # initialize three pointers
        # we search through the longer array, so if nums1 is longer, we swap arrays
        mid = left + (right - left) / 2 # we do not use (left + right) / 2 to prevent overflow

        def Binary(target, nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) //2
                if nums[mid] > target: # meaning target is on the left side
                    right = mid - 1
                elif nums[mid] < target: # target on the right side
                    left = mid + 1
                else:
                    return True # found the common value
            return False
        
        # Binary Search should be done on the longer array.
        # if nums1 is longer, call minCommonBinary to swap the array

        if len(nums1) > len(nums2):
            return self. minCommonBinary(nums2, nums1)
        
        # Search for each element of nums1 in nums2
        # return the minimum common value

        for num in nums1:
            if Binary(num, nums2) is True:
                return num
            
        return -1 # execute this block if none previous return happened
                

# Time Complexity: O(nlogm) where n is the length of nums1 and m the length of nums2
# Space Complexity: O(1)







