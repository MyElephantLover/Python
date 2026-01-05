# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# -- Inituition -- #
# by moving one pointer twice faster as the other pointer, when the fast
# pointer reaches the end of the list, the other pointer naturally lands on the middle node

from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

# Time Complexity: O(n) where n is the number of nodes in the linked list
# Space Complexity: O(1)

