# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

## -- Recursive DFS -- ##

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # base case
        if not root:
            return False
        
        # -- A path needs to be -- #
        # 1) from root to leaf
        # 2) only move down
        
        # if it's a leaf, check if the sum equals to targetSum
        if not root.left and not root.right:
            return root.val == targetSum
        
        # otherwise, check subtrees with remaining reduced target
        # we check remaining because this makes checking leaf easier
        complement = targetSum - root.val
        
        return self.pathSum(root.left, complement) or self.pathSum(root.right, complement) 

# Time Complexity: O(n) we visited each node once
# Space Complexity: O(h) for h is the maximum recursion stack (h = tree height). Worst case h is n

## -- Iterative DFS -- ##

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self. right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # first, define base case
        if not root:
            return False
        
        stack = [(root, targetSum - root.val)] # remaining sum

        while stack: # the loop ends when stack is empty
            # meaning we've done exploring all possible paths and if none of the above return happend
            # we return False
            node, remaining = stack.pop() # we check the most recent pair of node and remaining sum

            # if leaf, check remaining sum
            if not node.left and not node.right and remaining == 0:
                return True
            
            if node.right:
                stack.append((node.right, remaining - node.right.val)) # don't forget the .val

            if node.left:
                stack.append((node.left, remaining - node.left.val))
            
        return False

# Time Complexity: O(n) for n is the number of nodes in the tree
# Space Complexity: O(n) in the worst case, the recursive call stack can grow as big as the size of the tree
# which is a straight line
# for space complexity, we check the height of tree. The best case is a balanced tree where space complexity is O(logn)
# in iterative DFS, the worst case is a skewed tree, where space is O(n)






