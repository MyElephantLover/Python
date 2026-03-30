# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

## Idea: we need to explore the full island once we found a 1 (grid[i][j] == 1), use DFS or BFS
## we also need to mark visited cell so we do not count them twice

from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0]) # number of columns

        def dfs(i: int, j: int) -> int:
            # out of bounds or water
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0: # grid[i][j] == 1 is a land, 0 means 0
                return 0
            
            # mark as visited
            grid[i][j] = 0 # we turn land into water after visiting it: grid[i][j] == 0: return 0, so no infinite loop

            # current cell + 4 directions
            return (
                1 + dfs(i + 1 , j)
                  + dfs(i - 1, j)
                  + dfs(i, j + 1)
                  + dfs(i, j - 1)
            )
        
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i , j) # starting from this cell, explore the whole island and return its total size
                    max_area = max(max_area, area)

        return max_area

# Time: O(m * n) we visit each cell at most once
# Space: O(m * n) worst case recustion stack that every cell is an island (all values are 1)


