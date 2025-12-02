# In computer science, an in-place algorithm is an algorithm that operates directly on the input data structure without requiring extra space proportional to the input size.

class Solution:
    def Reverse_String(self, s:List[str])-> None:
        s.reverse()

# Time Complexity: O(n), n is the length of the string s
# Space Complexity: O(1) it is a constant space complexity since we do not use extra memory
