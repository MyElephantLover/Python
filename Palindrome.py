# Write a function to check if a string is a palindrome.

def isPalindrome(self, s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

## string manipulation, slicing


# Find the most frequent element in a list.

def mostFrequent(self, nums: List[int]) -> int:
    # use a hash map
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    return max(count, key=count.get) # find the key with the maximum count

# Use Counter

from collections import Counter

def findMostFrequent(self, nums: List[int]) -> int:
    return Counter(nums).most_common(1)[0][0] # most_common(1) returns the top 1 list, [(element, freq)] which is a list of tuple
    # most_common(1)[0][0] returns the final element


# Write a function to detect duplicates in an array.

def detectDuplicate(self, nums: List[int]) -> bool:
    seen = set() # to check for duplicates, the most common way is to use a set
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# Shorter Python Solution

def isDuplicates(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

# Set lookup is fast - O(1)

# Time: O(n) set lookup is O(1) and we check every element in the array
# Space: O(n) in the worst case, we store every element in the set
        
# Question 1 — Two Sum
# Given an array of integers nums and a target number, return the indices of two numbers that add up to the target.

def twoSum(self, nums: List[int], target: int) -> List[int]:
    counter = {} # create a hash map to store number -> index
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in counter:
            return [counter[compliment], i]
        
        counter[num] = i # store the current number as the key, and its index as the value

# Time: O(n)
# Space: O(n) in the worst case all elements get stored in the dictionary


# Question 2 — Valid Parentheses
# Check if parentheses are valid.

def checkParentheses(self, s: str) -> bool:
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}

    for ch in s:
        if ch in mapping: # closing brackets
            if not stack or stack[-1] != mapping[ch]: # mapping[ch] is a single character string, not a collection
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack # if the stack is empty it is valid parentheses

# Question 3 — Reverse a Linked List

from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next # save the next node
            curr.next = prev # reverse the pointer
            prev = curr # move the prev forward
            curr = next_node # move the curr forward

        return prev 


# Question 4 — Find First Unique Character

def firstUniqueCharacter(self, s: str) -> int:
    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i # return the index of ch
        
    return -1


# Question 5 — Merge Two Sorted Lists

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def mergeTwoSortedList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0) # fixed starting node, never moves
    curr1 = list1
    curr2 = list2
    tail = dummy

    while curr1 and curr2:
        if curr1.val <= curr2.val:
            tail.next = curr1 # tail always points to the last node in the merged linked list
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next

        tail = tail.next # advance tail everytime you attach a node

    # attach leftover
    if curr1:
        tail.next = curr1
    else:
        tail.next = curr2

    return dummy.next



