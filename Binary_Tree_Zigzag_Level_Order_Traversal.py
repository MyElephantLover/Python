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
        if not root:
            return []
            
        result = []
        queue = deque([root]) # a queue (FIFO) holds nodes we still need to process
            # what it does: 1) helps us do level-order traversal (BFS) ; 2) at any moment, contains all nodes for next level to process 
            # here we only use one side for adding and one side for removing
        left_to_right = True # a flag that controls directions (binary switch)
            # when it is True, keep left -> right; False: reverse

        while queue: # keep going as long as there're nodes left to process
                # we start with just the root node, and gradually add nodes level by level
                # Each iteration of this loop process one full level of the tree
            level_size = len(queue) # captures how many nodes are in the curr level
            level = [] # temp list to store values of node at the curr level;  after finishing the level, we append it to result

            for _ in range(level_size):
                node = queue.popleft() # takes next node to process (FIFO)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if not left_to_right: # this control the zigzag pattern per level
                level.reverse()

            result.append(level) # inside while loop because each level is a separate row in the result
            left_to_right = not left_to_right # it flips the direction / prepare the direction for the next level

        return result
        
# Time: O(n) where n is the number of nodes in the tree - it processes every node exactly once
# Space: O(n) where the result stores all nodes

            