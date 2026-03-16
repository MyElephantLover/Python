# 6. Write a function to check if a string is a palindrome.

def isPalindrome(self, s: str) -> bool:
    # s = s.lower().replace(" ", "") # convert to lowercase and remove whitespaces
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# 7. Find the most frequent element in a list.

def mostFrequent(self, nums: List[int]) -> int:
    count = {} # create a hash map to store the number -> freq

    for i, num in enumerate(nums):
        count[num] = count.get(num, 0) + 1 # dict.get(key, default) prevents errors if key does not exist

    return max(count, key = count.get) # find the key with the largest value

# 8. Write a function to detect duplicates in an array.

def isDuplicates(self, nums: List[int]) -> bool:
    # s = set(nums)
    return len(nums) != len(set(nums))

# Question 1 — Two Sum
# Given an array of integers nums and a target number, return the indices of two numbers that add up to the target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {} # create a hash map to store index -> number
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in count: # Python has O(1) on average for hashmap lookup
                return [count[compliment], i]
            count[num] = i # if not, we store the current number in the hash map

# Time: O(n) we visit each element in the array once
# Space: O(n) worst case the hash map has every element in the array

# Question 2 — Valid Parentheses
# Check if parentheses are valid.

class Solution:
    def validParentheses(self, s: str) -> bool:
        stack = [] # LIFO
        mapping = {')': '(', '}': '{', ']': '['} # mapping only contains closing brackets

        for ch in s:
            if ch in mapping:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else: #opening brackets
                stack.append(ch)

        return len(stack) == 0
    
# Question 3 — Reverse a Linked List

from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # prev represent a node reference, not a number
        curr = head

        while curr:
            next_node = curr.next # store the next node
            curr.next = prev
            prev = curr
            curr = next_node

        return prev # the new tail of the reversed list would be None
    
# Time: O(n) each node is visted exactly once
# Space: O(1) we only use a few pointer variables and no additional data strucutre is used

# Recursive solution

class Solution:
    def reverseLinkeList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive linked list reversal must stop at the tail, or it never terminate
        if not head or not head.next:
            return head
        
        new_head = self.reverseLinkeList(head.next)
        head.next.next = head # the next node should point back to the current node
        head.next = None
    
        return new_head
    
# Question 4 — Find First Unique Character, return its index, else return -1

class Solution:
    def firstUniqueCharacter(self, s: str) -> int:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
            
        return -1

# Time: O(n) as we traverse every chracter in the string once 
# Space: O(1) as the alphabet size is limited

# Question 5 — Merge Two Sorted Lists

class Solution:
    def mergeTwoList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # dummy node avoid empty list and head replacement
        curr1 = list1
        curr2 = list2
        tail = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val: # we add the smaller list to the merged list first
                tail.next = curr1
                curr1 = curr1.next # move curr1 forward
            else:
                tail.next = curr2
                curr2 = curr2.next

            tail = tail.next # move tail pointer forward; this needs to be inside the while loop so tail advance after each node attachment

        # adding leftover
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2

        return dummy.next # the new head of the merged list
    
# Time: O(n + m) where n is the length of list1 and m is the length of list2
# Space: O(1) because we reuse existing node and only create one dummy node

# Recursive Solution

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1 # at every step, we choose the smaller head node and recursively merge the rest
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
    # each recursive call solves merge(curr_head_node, remaining_list)
    # so each step shrinks the list

# Time: O(n + m)
# Space: O(n + m) because recursion use the call stack