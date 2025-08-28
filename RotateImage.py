class Solution:
    def rotate(self, matrix:List[List[int]])-> None:
        """
        Do not return anything. Modify in-place
        """
        n = len(matrix[0])

        ### The matrix is rotated layer by layer
        ### The outer loop is the rows we process
        ### Each element moves in its rotated position
        ### We only need to rotate one quadrant of the matrix
        ### to move all elements 

        for i in range(n // 2 + n % 2): ## row
            for j in range(n // 2): ## column
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - i]
                matrix[n - 1 - i][n - j - i] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

## Time Complexity: O(M) for M is the number of cells in the matrix
## Space Complexity: O(1) we do not use any other data structures



