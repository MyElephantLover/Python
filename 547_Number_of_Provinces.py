# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

from collections import defaultdict
class Solution:
    def numberOfProvince(self, isConnected: List[List[int]]) -> int:
        counter = 0
        seen = set() # seen stores integers, and each integer is a city id (node id)

        def dfs(node):
            # if node not in seen:
            #     seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor) # we need to first add neighbor to seen, then recurse from it, bc dfs() needs to go through all neighbors
                    dfs(neighbor)
        # build the graph
        n = len(isConnected) # n is the length of the matrix
        graph = defaultdict(list)
        for i in range(n): # nodes in a graph are just indices of a matrix
            # we don't store objects, or edges, just the node ids
            for j in range(i + 1, n): # we only look at the upper triangle of the matrix to advoid duplicates
                if isConnected[i][j]: # if isConnected[i][j] == 1 or 0:
                    graph[i].append(j) # for each connection (i,j) we add each direction manually
                    graph[j].append(i) # we add both directions bc graph is undirected

        """
        adjacency list representing a graph

        graph = {
                key: [value]
                1: [2, 0],
                2: [3, 4]
                3: []
        }
        
        
        """

        """
          j (gt i to n)
        i
          0 1 2 
          1
          2
        
        """

        for i in range(n):
            if i not in seen: # if city i has not been assigned to a province yet, it starts a new province
                # add all nodes of a connected component to the set
                counter += 1 # when do we know we've found a new province? if i not in seen, it must start a new province
                seen.add(i) # mark the starting city as visited
                dfs(i) # explore its neighbors

        return counter


# Time Complexity: O(n^2) DFS is O(V + E) and the dominant part is the edges can be up to O(n^2)
# Space Complexity: O(n^2): O(n) for the set, but graph can store up to O(n^2) edges. 
                    

