# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Here we care about the number of edges on the longest path between any given two nodes
# At every node, the longest path through that node = height(left subtree) + height(right subtree)
# This could be the diameter

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        # use DFS search
        # each node has two jobs
        # 1) update its global diameter
        # 2) return its height to its parent
        # height = # of edges from this node down to the deepest leaf
        self.diameter = 0

        def dfs(node): # here it defines the function
            # base case
            if not node: # Null nodes compute 0 height - diameter counts edges not nodes
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # update diameter at this node
            # This is the essence of the problem
            self.diameter = max(self.diameter, left_height + right_height)

            # return height of this subtree
            return 1 + max(left_height, right_height) # the parent node needs your height to compute its diameter
        
        dfs(root) # dfs() is designed to return height
        # here it starts the recursion - traverse the whole tree
        return self.diameter # global variable - stores this across all nodes
    
# Time: O(n) where each node is visited once
# Space: O(h) where h is the height of the recursion stack


