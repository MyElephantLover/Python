# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

# Constraints:

# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000

# Idea: Treat the tree like an undirected graph:
# Each node connects to left, connects to right, and each children can go back to its parent

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def all_nodes_distance(self, root: Optional[TreeNode], target: Optional[TreeNode], k: int) -> List[int]:
        # base case
        if not root: # if the tree is empty, there are no nodes at any distance
            return []
        
        parent = {} # we build a parent map
        target_node = None # start with None

        # step1: DFS to record each node's parent, and find the actual target node
        def dfs(node: Optional[TreeNode], par: Optional[TreeNode]) -> None:
            # we pass the parent downward as we recurse
            nonlocal target_node # target_node is defined outside of this function
            
            if not node:
                return # stops recursion when we hit a leaf's child (None)
            
            parent[node] = par # build parent map; we don't need nonlocal here 
            # as we are modifying an object, not reassigning variables
            if node == target:
                target_node = node # updates the outer variable
            
            dfs(node.left, node) # go to the left and right child, and tell them node is their parent
            dfs(node.right,node)

        dfs(root, None) # instead of returning anyting, it modifies variables outside of the function
        # it modifies: 1) parent (dictionary); 2) target_node (variable)

        if not target_node:
            return []
        
        # Step2: BFS starting from target_node
        # we need a queue to explore level by level
        # we need a visited set to avoid going in circles
        # a result list
        queue = deque([(target_node, 0)]) # we are running BFS starting from the target_node
        # a tuple (node, distance_from_target)
        # becoz the quesition asks nodes at distance of k - we need to track the distance we've traveled
        visited = {target_node} # a set
        result = []

        while queue:
            node, dist = queue.popleft()

            if dist == k: # we've reached a node that's exactly k steps away from the target
                result.append(node.val)
                continue # stops the loop, we do not explore this node's neighbors, becoz we want to stop at exactly k

            for neighbor in (node.left, node.right, parent[node]): # from the curr, look at all possible nodes we can move to
                # why a tuple? just a quick way to group all neighbors
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1)) # becoz we need to traverse nodes, not just store values
                    # neighbor is a TreeNode object

        return result


        # Time: O(n) DFS: build parent map; BFS: visit every node at most once -> O(n) + O(n) = O(n)
        # Space: O(n) parent dictionary stores all nodes; BFS queue up to O(n); recursion stack up to O(h) but smaller than O(n)





