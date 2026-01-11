# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Constraints:

# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000

# -- recursion dfs -- #
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        
        # if at the leaf node: leaf node has dpeth 1
        if not root.left and not root.right:
            return 1
        
        # if skewed tree - only one side has child
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # if both sides have children
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    
# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of call stack (base case: logn; worst case: n)

# -- BFS (level order): BFS stops right after finding a first leaf -- #
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        
        # we stores (node, depth) in a queue: the queue is a list of future work
        # so we need to wrap the tuple in a list
        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft() # queue FIFO - we pop one, check it(remove the current node to inspect), and if it's not a leaf
            # we add its children to the queue to check later

            if not node.left and not node.right: # a leaf node
                return depth # BFS checks nodes level by level. from qq: the first leaf node we encounter quaranteed to be the min depth
            
            if node.left: # skewed tree: this line only runs if left child exists
                queue.append((node.left, depth + 1)) # BFS checked its children after all nodes at the current levels
                # the child is one level depper than the parent, we want to remember which node to check, and what its depth is
                # when we eventually process this child, the depth would be parent depth + 1

            if node.right: # this line only runs if right child exists
                queue.append((node.right, depth + 1))

# Time Complexity: O(n) for n is the # of nodes; each node enters and leave the queue once
# Space Comeplxity: O(n) this dominated by the queue; worst case the last level contains n/2 nodes; queue can have many nodes at once
# BFS is usually faster than DFS bc it checks all nodes at the current level - it stops after finding the first leaf
