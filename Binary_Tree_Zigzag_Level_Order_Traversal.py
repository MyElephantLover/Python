# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def binary_tree_zigzag(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node):
            if not node:
                return []
            
            result = []
            queue = deque([root]) # a queue (FIFO) holds nodes we still need to process
            # what it does: 1) helps us do level-order traversal (BFS) ; 2) at any moment, contains all nodes for next level to process 
            # here we only use one side for adding and one side for removing
            left_to_right = True # a flag that controls directions (binary switch)
            # when it is True, keep left -> right; False: reverse

            while queue: # keep going as long as there're nodes left to process
                # we start with just the root node, and gradually add nodes level by level
                level_size = len(queue)
                level = [] # temp list to store values of node at the curr level;  after finishing the level, we append it to result

                for _ in range(level_size):
                    node = queue.popleft()
                    level.append(node.val)

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                if not left_to_right:
                    level.reverse()

                result.append(level)
                left_to_right = not left_to_right # it flips the direction

            return result
        
# Time: O(n) where n is the number of nodes in the tree - it processes every node exactly once
# Space: O(n) where the result stores all nodes

            