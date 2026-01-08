# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use a dummy node
        dummy = ListNode(0, head)
        prev = dummy # prev is the moving pointer while dummy is a fixed anchor to spicify the position for head

        while prev.next is not None and prev.next.next is not None: # when prev not run out of node, prev is the cursor
            first = prev.next # define connections - connecting nodes
            second = first.next

            # swap
            # prev -> a -> b -> next
            # prev -> b -> a -> next
            first.next = second.next
            second.next = first
            prev.next = second

            # move prev forward
            prev = first

        return dummy.next 
            
# Time Complexity: O(n) for n is the number of nodes in the linked list
# Space Complexity: O(1) since we use constant number of pointers


