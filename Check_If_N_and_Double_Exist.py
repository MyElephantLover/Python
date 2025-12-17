# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Constraints:

# 2 <= arr.length <= 500
# -103 <= arr[i] <= 103

# Brute Force #
class Solution:
    def checkExist(self, arr: List[int]) -> bool:
        # Brute Force approach is to iterate over the array with separate index
        # initialize variables
        n = len(arr)

        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    continue
                if arr[i] == 2 * arr[j]:
                    return True
        return False # if none of the above return happened, return False
    # remember that "return" returns the entire function immediately, not just the function
    
# Time Complexity: O(n^2) where n is the length of the arr
# Space Complexity:O(1)

# Use a Set #

class Solution:
    def checkDouble(self, arr: List[int]) -> bool:
        # a set is to store all unique numbers we've checked so far
        # we iterate through the array to check if 

        Set = set() # this is an empty set
        n = len(arr)

        for i in range(0, n):
            if 2 * arr[i] in Set or (arr[i] % 2 == 0 and arr[i] // 2 in Set):
                return True
            Set.add(arr[i]) # if not seen in Set, this means we have not processed this element
            # hence, we add it to the set

        return False # if none of the above return happened, return False
    
# Time Complexity: O(n), sort function takes O(nlogn)
# Space Complexity: O(n) for the set 

# Binary Search

# The concept of binary search is we set a target value and compare that with the middle point
# hence, we have left, right and mid pointers

class Solution:
    def removeDuplicates(self, arr: List[int]) -> bool:
        # initialize variables
        arr.sort() # for binary search to work, we need to sort the array first
        n = len(arr)

        for i in range(0, n):
            target = 2* arr[i]
            index = self._custom_binary_search(arr, target)
            if index >= 0 and index != i: # meaning there is an index satisfying 2 * arr[index] == arr[i]
                # index != i means i != j
                return True
            return False
        
    def _custom_binary_search(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        mid = left + (right - left) // 2 # the formula to advoid integer overflow
        while left <= right:
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1 # using left -= 1 would cause infinite loop (while left <= right)
            else:
                right = mid - 1

        return -1 # target not found

# Time Complexity: O(nlogn) for the sorting algorithm
# Space Complexity: O(n) Python uses a sort algorithm which is a combination of merge sort and insert sort 
# which takes O(n) memory








