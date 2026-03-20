# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Idea: A node is valid if: 1) it is greater than everything allowed on the left bound ; 
# 2) It is less than everything allowed on the right bound 

from typing import Optional
class Solution:
    def validateBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node: # an empty tree is considered a valid BST - base case
                return True
            
            if not(low < node.val < high):
                return False
            
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
            # everything in the left subtree must be greater than low and less than node.val
            # everyhting in the right subtree must be greater than node.val and less than high
        
        return dfs(root, float("-inf"), float("inf"))
    
# Time: O(n) for n is the number of nodes in the tree
# Space: O(h) for h is the height of the recursive call stack
