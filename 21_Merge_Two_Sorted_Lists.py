# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

class Solution:
    def mergeLinkedList(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        # the idea is
        # 1) create a dummy node to start the merged list
        # 2) use the pointer tail to build the result
        # 3) compare curr1.val and curr2.val
        # 4) attach the smaller node to tail
        # 5) move the list pointer, tail, forward
        # 6) when one list ends, attach the remaining nodes

        dummy = ListNode(0)
        tail = dummy # tail is the pointer we use to extend the merged list
        # tail always points to the last node of the linked list

        curr1 = head1
        curr2 = head2

        while curr1 and curr2: # while loop stops as soon as one of the list becomes empty, but there might be nodes left in the other listS
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next

            tail = tail.next # the tail pointer updates after either branch executes

        # attach remaining nodes - only one list can have nodes left, since both lists are sorted, the remaining nodes
        # can be appended directly without further comparison
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2

        return dummy.next # when we merge nodes, we attach them after the dummy, so the real merged list starts after the dummy

# Time: O(n + m) where n is the length of list1 and m is the length of list2
# Space: O(1)

        


