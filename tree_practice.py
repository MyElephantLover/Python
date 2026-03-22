# def fn(root: TreeNode, x: int) -> int:
#     if not root:
#         return 0
#     ans = 1 if root.val == x else 0 # A
#     ans += fn(root.left, x)
#     ans += fn(root.right, x)
#     return ans

# This function is implementing DFS. How would you implement BFS to solve the same problem?

from collections import deque
from typing import Optional

def fn(root: TreeNode, x: int) -> int:
    if not root:
        return 0
    
    queue = deque([root])
    count = 0

    while queue:
        node = queue.popleft()

        if node.val == x:
            count += 1
        
        if node.left: # if this node has a left child
            queue.append(node.left) # append() add from right; appendleft(), popleft(), pop()

        if node.right:
            queue.append(node.right)

    return count

