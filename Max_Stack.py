## Referring to Min_Stack.py, let's try to implement Max Stack

class MaxStack:
    def __init__(self): # init creates an object MaxStack
        self.stack = [] # create an empty list to store elements in the stack
                        # each element is (val, curr_max_so_far)
    def push(self, val: int) -> None:
        # so here we want to store the tuple (val, curr_max) in the stack
        # so we could use O(1) to getMax

        if not self.stack: # if the stack is empty
            self.stack.append((val, val)) # the curr_max is val
            return # end the loop
        
        current_max = self.stack[-1][1] # we store the curr_max aside
        new_max = max(val, current_max)
        self.stack.append((val, new_max))

    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMax(self) -> int:
        return self.stack[-1][1]
    
# In Python, list[-1] means the last element in the list, which is the same
# as peek() in Java and other languages

# Time Complexity: O(1) as all operations are O(1)
# Space Compelxity: O(n) as worst case all operations are push, which leads to O(2n)




