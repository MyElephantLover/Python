# There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

# Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

# Note that node 0 will not be a restricted node.

# Constraints:

# 2 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges represents a valid tree.
# 1 <= restricted.length < n
# 1 <= restricted[i] < n
# All the values of restricted are unique.

## Ideas: 
# 1) build an adjacency list from edges; 
# 2) put restricted into a set for fast lookup
# 3) start DFS from node 0
# 4) count every node you can visit w/o entering a restricted node 

from typing import List
from collections import defaultdict
class Solution:
    def reachableNodes(self, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)

        # build the undirected graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        restricted_set = set(restricted)

        def dfs(node: int, parent: int) -> int:
            if node in restricted_set:
                return 0
            
            count = 1 # count this node

            for neighbor in graph[node]:
                if neighbor != parent: # avoid going backwards
                    count += dfs(neighbor, node) # because we came from node
            
            return count
        
        return dfs(0, -1) # start DFS at node 0, and it has no parent; node labels are from 0 to n - 1
                            # so -1 is guaranteed to not be a real node, just a dummy value
    
# Time: O(nodes + edges) = O(n + (n - 1)) = O(n) each node is visited once
# Space: O(n) where n is the worst case recustion stack (skewed tree)




        
        
        
        def dfs(i : int, j : int) -> int:

