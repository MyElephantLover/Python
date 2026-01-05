class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
# Write your code here
# Try creating 1 <-> 2 <-> 3
# Test with print()

# create the nodes

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# connect the three separate nodes together forwards and backwards
head = node1
node1.prev = node2
node2.next = node3

tail = node3
node3.prev = node2
node2.next = node3

# use a dummy pointer for head as we want to always be able to access head
current = head
while current:
    print(current.val)
    current = current.next

while tail:
    print(tail.val)
    tail = tail.prev

# using a Linked List, when we have a pointer at the position we want to operate on, the time complexity 
# for insert / delete is O(1) given direct access to the node (we only need to change the position of the node, prev and next)

# if not, finding the node takes O(n) and after that insertion and deletion takes O(1)