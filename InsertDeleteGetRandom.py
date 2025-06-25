from random import choice

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here
        """
        self.dict={}
        self.list = []

    def insert(self, val:int) -> bool:
        """
        Insert a element to the set. Returns false if the element already in the set
        """
        if val in self.dict:
            return False
        # otherwise, insert the element in the set

        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
    
    def remove(self, val:int) -> bool:
        """
        Return True if the element is in the set
        How we delete is we get the index to delete from the HashMap / Dictionary
        Then we move the last element to the index to remove
        Lastly, we pop the last element out of the dict
        """
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val] # we get the last element and index
            self.list[idx], self.dict[last_element] = last_element, idx 
            # we move the last element to the position where we removed the element
            # The above line is to fill the values to the keys, where the self.list[idx] is the index
            # we remove the original value, and we filled it with the last element
            self.list.pop() # delete the last element
            del self.dict[val]
            return True
        return False
    
    def GetRandom(self) -> int:
        # Get Random could be implemented in O(1) time with the help of standard random.choice in Python
        # and Random Object in Java
        return choice(self.list)
    
# Time Complexity: GetRandom is always O(1), and insert and delete are both O(1). In the worst case, 
# we get O(n) when it exceeds the allocated storage in the HashMap / Array and invoke the extra space
# reallocation
# Space Complexity: O(n) to store N elements





        
        

