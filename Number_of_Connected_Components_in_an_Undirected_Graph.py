# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

from typing import List
class Solution:
    def numberOfConnectedComponents(self, n: int, edges: List[List[int]]) -> int:
        # building the graph, adjacency list
        # for examplem, we want to convert something as below
        # n = 5, edges = [[0, 1], [1, 2], [3,4]]
        # into: 
        # graph = {
        # 0: [1],
        # 1: [0, 2],
        # 2: [1],
        # 3: [4]
        # 4: [3]}
        # first step: create an empty graph, this is dictionary comprehension
        graph = {i: [] for i in range(n)}

        for a, b in edges: # we loop through all edges -> O(e)
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node: int) -> None: # this function does not return anything
            # what dfs() does:
            # 1) it modifies visited
            # 2) recursively explore nodes
            # 3) does not return a value
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        count = 0
        for node in range(n): # each node is visited once -> O(n)
            if node not in visited:
                count += 1
                dfs(node)

        return count
    
# Time: O(n + e) where e is the number of edges
# Space: O(n + e)



