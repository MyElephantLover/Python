# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

# Constraints:

# 1 <= arr.length <= 1000
# 0 <= arr[i] <= 1000

class Solution:
    def countElement(self, arr: List[int]) -> int:
        # initialize variable
        cnt = 0 # use to store how many x's
        Set = set(arr) # store unique values in arr

        for x in arr: # loop over arr makes sure duplicates being counted separately
            if x + 1 in Set: # if we use "if x + 1 in arr:" membership check in a list takes O(n), so time complexity would be suboptimal
                cnt += 1
        return cnt
    
# Time Complexity: O(n): membership check in Set on average takes O(1), we iterate all elements in arr which is a list
# so in total time complexity is O(n)
# Space Complexity: O(n): maximum size of the set is n

