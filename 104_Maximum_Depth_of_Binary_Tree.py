# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 
from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: # if current node does not exist, this gives the def of maximum depth that, an empty node's depth is 0
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# Time Complexity: O(n) where n is the number of nodes in the tree 
# Space Complexity: O(h) where h is the recursive stack height; the recursive stack means that each
# time the recursive call happens, Python pauses the current function and saves the local variables
# return address, puts that on the call stack (so it can visit later). this stack grows with the recursive calls.
# The deepest height of the stack is the depth from the root to the leaf


