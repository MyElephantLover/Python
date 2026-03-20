# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def min_absolute_difference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.prev = None # use self.prev when we want the variable to persist across function calls inside a class
        self.min_diff = float("inf") # these are instance variables, they belong to the object (Solution) and shared across all recursive calls
        def dfs(node):
            if not node: # if node is None, we stop
                return
            
            dfs(node.left)

            if self.prev is not None: # self.prev stores previous values we visited
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val # after processing the curr node, we update prev to be the curr value

            dfs(node.right)

        dfs(root)
        return self.min_diff
    
# Time: O(n) where n is the number of nodes in the tree, and we visit each node exactly once
# Space: O(h) where h is the height of the recursive stack




