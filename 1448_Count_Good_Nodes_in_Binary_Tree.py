# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Constraints:

# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
import math
class Solution:
    def countGoodNodes(self, root: Optional[TreeNode]) -> int:
        # a good nodes means from the root to the current node, there is no value gt the current node

        # base case
        if not root:
            return 0
        
        # maxSoFar = 0 # we define this interger to store and update the maximum value from root to curr

        def dfs(node: Optional[TreeNode], maxSoFar: int) -> int: # this dfs helper function
            # do the recursion and carries extra state, maxSoFar
            # base case
            if not node:
                return 0
            
            if node.val >= maxSoFar:
                good = 1 # good is an indicator here to dictate if the curr node is good
                new_max= math.max(node.val, maxSoFar) # we use new_max here to advoid accidentally change the parent's parameter
            else:
                good = 0

            return good + dfs(node.left, new_max) + dfs(node.right, new_max) # the actual counting happens here

        return dfs(root, root.val) # the public API, countGoodNodes only runs once and return the count
    
# Time Complexity: O(n) for n is the number of nodes in the tree
# Space Complexity: O(n) for worst case, n is the longest recursion call stack height



        
