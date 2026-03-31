# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

# Idea: Use BFS - since every move has the same cost, BFS finds the shortest path first

from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # start or end blocked
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0: # we can only walk on cells with value == 0
            return -1
        
        # single cell case
        if n == 1:
            return 1
        
        # think of a cell like a center of the tic-tac-toe board
        # \.   |.   /
        # <- center ->
        # /.   |.   \
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        q = deque([(0, 0, 1)]) # row, column, path length / deque object is open-ended queue
        # each element is a tuple (row, col, distance-so-far)
        visited = {(0, 0)} # a set with one element, the tuple (0, 0)

        while q:
            r, c, dist = q.popleft() # row, col, distance-so-far
            # dist = number of cells visted to reach (r, c)

            if r == n - 1 and c == n - 1: # checking if we meet the destination (n - 1, n - 1), the bottom right corner
                return dist

            for dr, dc in directions: # try every possible directions
                nr, nc = r + dr, c + dc # each dr, dc are move directions
                # one direction can be dr = -1, dc = 0 which is move up
                # r, c current positions
                # nr, nc: neighbors - cells after moving

                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc, dist + 1)) # because we are moving one step further to neighbors

        return -1
    
# Time: O(n^2) where n is the length of the grid. Each cell is visted at most once
# Space: O(n^2) worst case the visted set stores up to n^2 cells
