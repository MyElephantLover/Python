# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

class MinStack:
    def __init__(self):
        self.stack = [] # we initialize an instance variable called stack, and create an empty list to store elements in the stack

    def push(self, val:int) -> None: # push means to add elements to the stack
        if not self.stack: # if the stack is empty, the curr_min_value would be the same as the value just added
            self.stack.append((val, val))
            return # to stop the function early
        
        # otherwise, calculate the curr_min
        current_min = self.stack[-1][1]
        self.stack.append(val, min(val, current_min))

    def pop(self) -> None: # pop() removes the element from the stack
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1, 0]
    
    def getMin(self) -> int:
        return self.stack[-1, 1] # the min up to the top point has already been calculated
    
    # Time Complexity: O(1) for all operations
    # Space Complexity: O(n) for worst-case all operations are push, there would be
    # O(2n) used
    


