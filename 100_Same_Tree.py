# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # hint:
# If p and q are the same tree, then the following is true (if and only if):
# p.val = q.val
# p.left and q.left are the same tree
# p.right and q.right are the same tree

        # base case
        # we treat p and q as the roots and declare all conditions that make them not the ame
        # if none of these applies, we check their left and right subtrees

        if not p and not q:
            return True
        
        if not p or not q: # if either one does not exsit, there is no same tree
            return False
        
        if p.val != q.val:
            return False
        
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
    
## -- Iterative DFS -- ##
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we iteratively check the conditons that make them not the same
        # return True at the end if none of the above return False happened

        stack = [(p, q)] # we treat p, q as roots

        while stack: # before stack goes empty, meanining finished all the explore
            node1, node2 = stack.pop()

            if node1 is None and node2 is None: # both None, continue checking others
                # return True 
                continue # because recurstion ensures all paths are checked, so it returns True in recursion

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            # if none of the above happens

            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True # in iterative dfs, return True only happens after the stack is fully processed
    
# Time Complexity: O(n + m) for n, m is the number of nodes in p and q
# Space Complexity: O(n + m) for n and m is the maximum height of the respective call stack