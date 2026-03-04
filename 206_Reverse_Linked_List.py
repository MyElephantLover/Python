# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the idea is
        # 1) save the next node
        # 2) move the prev forward
        # 3) move the curr forward

        prev = 0
        curr = head

        while curr: # when curr becomes None, we exit the loop
            next_node = curr.next # store the next node
            curr.next = prev # reverse the pointer
            prev = curr # move the prev forward
            curr = next_node # move the curr forward

        return prev # the new head is the node stores in prev
    # prev is the new list
    # curr is remaining list, when curr is empty, the new list is complete
    
# Time: O(n)
# Space: O(1) as we reverse in place


# Recursive solution

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head # take the next node, and make it point back to the current node
        head.next = None # then cut the old forward connection

        return new_head

# Time: O(n) each node is visted exactly once
# Space: O(n) the recursive call stack has the depth of n. Each recursive call is stored in the call stack until the base case is reached

# Why iterative solution is better - 1) constant memory; 2) avoid recursion stack overflow for large lists 