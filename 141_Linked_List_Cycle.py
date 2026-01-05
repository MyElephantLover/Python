# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def linkedListCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None: # make sure fast.next is not null
            slow = slow.next # move 1 step
            fast = fast.next.next # move 2 steps

            if slow is fast:
                return True
            
        return False
    
# Time Complexity: O(n) where we traverse the linked list once (worst case is the fast pointer traverses the list)
# even with a cycle, the two pointers meet after at most a linear number of steps
# Space Complexity: O(1) we do not allocate extra data structure