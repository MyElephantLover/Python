# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# Idea: Use binary search over the matrix as if it were in the sorted array
# Because: 1) each row is sorted 2) each row starts after the previous row ends
# # the whole matrix is effectively sorted in row-major order 

from typing import List
class Solution:
    def search2Darray(self, matrix: List[int][int], target: int) -> bool:
        m = len(matrix) # number of rows in a matrix
        n = len(matrix[0]) # number of columns in each row

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            # think of a matric as a flattened array
            row = mid // n # each row has n elements
            col = mid % n
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
    
# Time: O(log (m * n)) because we are doing one binary search over (m * n) elements
# Space: O(1)
