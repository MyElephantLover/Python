# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 109
# -109 <= target <= 109

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def closestBSTValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        node = root # node is a TreeNode object

        while node:
            # update closest if this node is better, or the same closest but smaller
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
            elif abs(node.val - target) == abs(closest - target):
                closest = min(node.val, closest)

            # Use BST property to move left or right - we do not have to blindly search both sides
            # at each node, we only move one direction based on target
            if target < node.val: # meaning every node on the right is guaranteed to be worse than the left subtree (node.right > node.val > target)
                node = node.left # move to the left child node, changing the position in the tree
            elif target > node.right:
                node = node.right
            else:
                return node.val # extactly the same
            
        return closest
    
# Time: O(h) where h is the tree height
# Space: O(1) we only use a few variables, node and closest, no recursion and no additional data structure
    
# Recursive solution

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def closestBSTValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node, closest):
            if not node:
                return closest
            
            # compare node.val and closest
            if abs(node.val - target) < abs(node.val - closest):
                closest = node.val
            elif abs(node.val - target) == abs(node.val - closest):
                closest = min(node.val, closest)
            # the else means the current node is worst than the best we've seen, so do nothing
            # we skip the else; this is the same as pass
            
            if target < node.val: # meaning the right subtree will be greater than node.val and target
                return dfs(node.left, closest)
            elif target > node.val:
                return dfs(node.right, closest)
            else:
                return node.val
            
        return dfs(root, root.val)
    
# Time: O(h) where h is the height of the BST; instead of visting all nodes, we visited at most one node per level
# Space: O(h) where h is the height of the tree; each recursive call represent a stack frame
    
            



            



            