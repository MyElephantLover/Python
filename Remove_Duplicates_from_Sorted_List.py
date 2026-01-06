# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next # since the list is sorted, we only move forward, there's no prev in our linked list

class Solution:
    def removeDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # since the list is sorted, we just need to compare cur.val versus cur.next.val
        # and skip duplicates

        cur = head

        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                # skip the duplicated node
                cur.next = cur.next.next
            else:
                cur = cur.next # this means move the reference cur to the next node
                # we only move when there is a different value
        return head


# Time Complexity: O(n) where n is the number of nodes in the list, we only traverse the linked list once
# Each node is visited at most one time. Even with duplicates, we only adjust pointers, not re-traverse
# Space Complexity: O(1) because we do not use extra data structures, e.g. set, hashmap. only a constant number of pointers

