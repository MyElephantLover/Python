# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

from collections import defaultdict, UserList
class Solution:
    def findPathExists(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # build the graph

        graph = defaultdict(list)
        for u, v in edges:
            graph.append(u)
            graph.append(v)

        # iterative DFS
        visited = set([source]) # [source] is an iterable
        stack = [source] # stack is a list

        while stack: # when there are nodes left to explore
            node = stack.pop()
            if node == destination: # source node changes but destination node not, this means we've reached the destination node
                return True
            # explore neighbors
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        # if none of the above happend
        return False
    
# Time: O(n) for n is the # of nodes
# Space: O(h) for h is the height of the recursion stack
