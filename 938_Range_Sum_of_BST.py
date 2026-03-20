# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Constraints:

# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def range_sum_of_BST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        # if root value is smaller than low, only right subtree can have valid values
        if root.val < low:
            return self.range_sum_of_BST(root.right, low, high)
        
        # if root value is greater than high, only left subtree can have valid values
        if root.val > high:
            return self.range_sum_of_BST(root.left, low, high)

        # root is in range, include it and search both sides

        return (root.val + self.range_sum_of_BST(root.left, low, high) + self.range_sum_of_BST(root.right, low, high))
    
# Time: O(n) where n is the number of nodes in the tree - in the worst case, every node falls within [low, high] - we traverse every node
# Space: O(h) where h is the height of the tree - we are using recursion, which uses the call stack
# space depends on tree height - a balanced tree is O(logn); a skewed tree is O(n)
    






