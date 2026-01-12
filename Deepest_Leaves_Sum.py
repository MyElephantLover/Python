# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int: # deepestLeavesSum() is a class method
        # define sentinel values
        deepest = -1 # the depth from root is 0, we specify that we have not visited any node yet
        total = 0

        def dfs(node, depth): # dfs() is a local function
            # base case
            if not node:
                return
            
            # if its a leaf
            if not node.left and not node.right:
                if depth > deepest:
                    deepest = depth
                    total = node.val # new deepest level: reset
            elif depth == deepest:
                deepest = depth
                total += node.val # same deepest level: add

            # if none of the above happend
            return
        
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return total

# Time Complexity: O(n) for n is the # of nodes
# Space: O(h) for h is the height of recursion call stack