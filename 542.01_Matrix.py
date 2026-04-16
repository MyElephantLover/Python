# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two cells sharing a common edge is 1.

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

from ast import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # base case
        if not mat:
            return []
        
        m, n = len(mat), len(mat[0]) # m is number of rows, n is number of columns
        queue = deque() # we will use this for BFS
        visited = set() # we will use this to avoid going in circles

        # step1: add all the 0s to the queue and mark them as visited
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0)) # we also add the distance (0) to the queue
                    visited.add((i, j)) # mark this cell as visited

        # step2: BFS from all the 0s at the same time
        while queue:
            i, j, dist = queue.popleft() # get the current cell and its distance from the nearest 0
            
            # we will explore its neighbors (up, down, left, right)
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj # calculate neighbor's coordinates
                
                # check if the neighbor is within bounds and not visited
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited: 
                    # ni is row index, nj is column index
                    # ni must be greater than or equal to 0 and less than m (number of rows)
                    # nj must be greater than or equal to 0 and less than n (number of columns)
                    # and the neighbor must not have been visited before
                    visited.add((ni, nj)) # mark neighbor as visited
                    mat[ni][nj] = dist + 1 # update neighbor's distance to nearest 0
                    # the above line means the distance from this cell, to the nearest 0 is dist + 1
                    # because we are at the current cell (i,j) and its dist to the nearest 0 is dist
                    # and the neighbor (ni, nj) is one step away from (i, j), so its distance to the nearest 0 is dist + 1
                    queue.append((ni, nj, dist + 1)) # add neighbor to the queue with updated distance

        return mat
    
# Time: O(m*n) - we visit each cell at most once in the BFS, and we also iterate through the matrix once to add the 0s to the queue. So overall O(m*n).
# Space: O(m*n) - in the worst case, if all cells are 0s, we will add all of them to the queue and visited set. So O(m*n).
