# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

# Constraints:

# The number of nodes in the tree is in the range [2, 5000].
# 0 <= Node.val <= 105


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDifference(self, root: TreeNode) -> int:
        # At any node, the largest ancestor difference involving that node is
        # 1) abs(node.val - path_min)
        # 2) abs(node.val - path_max)
        # so in DFS - update path_min and path_max and keep going
        # DFS(Depth First Search) is traverse all the nodes as deepest as possible and then backtrack

        def dfs(node, path_min, path_max):
            if not node:
                return path_max - path_min
            
            path_min = min(node.val, path_min)
            path_max = max(node.val, path_max)

            left_ans = dfs(node.left, path_min, path_max)
            right_ans = dfs(node.right, path_min, path_max)

            return max(left_ans, right_ans)
        
        return dfs(root, root.val, root.val) # start with root.val as both the path min and path max
    
    # Time: O(n) as each node is visited once
    # Space: O(h) for recursive stack, h is the tree height

    
    

    