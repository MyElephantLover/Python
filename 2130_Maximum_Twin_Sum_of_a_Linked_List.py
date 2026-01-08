# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Constraints:

# The number of nodes in the list is an even integer in the range [2, 105].
# 1 <= Node.val <= 105

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def maxTwinSum(self, head: Optional[ListNode]) -> int:
        # find the middle pointer - slow ends at the start of the second half for even length
        fast = head
        slow = head
        # dummy = ListNode(0, head)
        # prev = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # revert second half starting at slow
        prev = None
        curr = slow # reference curr to the slow pointer
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # now prev is the head of the second half

        # compute max twin sum
        max_sum = 0
        first = head 
        second = prev
        while second: # keep going as long as the second pointer is not None
            # so this loop over every node in the second reversed half
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
    
# Time Complexity: O(n) for n is the number of nodes in the list 
# Space Complexity: O(1) as we only use a constant number of pointers do not create extra data structure


    
