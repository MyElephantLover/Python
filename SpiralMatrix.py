class Solution:
    def spiralOrder(self, matrix:List[List[int]])-> List[int]:
        # initialize rows and columns
        # initialize boundary as left, right, up and down
        # initialize result array as result

        result = []
        rows, columns = len(matrix), len(matrix[0])
        left = up = 0
        right = columns - 1 # the index is the length - 1 because Python is 0-indexing
        down = rows - 1

        while len(result) < rows * columns: # not reach the boundary
            # traver from left to right
            for col in range(left, right + 1):
                result.append(matrix[up][col])
            # from up to down
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # make sure on the diff row
            if up != down:
                # traver from left to right
                for col in range(right - 1, left - 1, -1): # since the step is negative, it stops once it get past left
                    # step = -1 means iterates backwards
                    result.append(matrix[down][col])

            # make sure on diff col
            if left != right:
                # traverse upwards
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1 # from left to right
            right -= 1 # from right to left
            up += 1 # move upwards
            down -= 1 # moving downwards
        
        return result

# Time Complexity: O(M * N) where M is the number of rows and N is the number of columns
# Space Complexity: O(1) we do not include result array in the space complexity 



