class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # initially, my intuition was to loop through the source string, see if all of them exist
        # in the target string, but in this problem, order matters
        # So, intuition is to use Devide and Conquer with Greedy, meaning to break problem
        # into smaller subproblems and solve each subproblems and apply it recursively

        LEFT_BOUND = len(s)
        RIGHT_BOUND = len(t)

        def rec_isSubsequence(left_index, right_index):
            # base cases
            # we define two base cases - the one is the source string becomes empty
            # the other one is the target string becomes empty

            if left_index == LEFT_BOUND:
                return True # exhaust source string
            if right_index == RIGHT_BOUND:
                return False # target string becomes empty first, left unmatched letters in the source string
            
            if s[left_index] == t[right_index]: # The first character match on the source & target
                left_index += 1
            right_index += 1 # otherwise, continue with the target string to see where we can match with 
            # the first character in the source string

            return rec_isSubsequence(left_index, right_index)
        
        return rec_isSubsequence(0 , 0)
    
    # Time Complexity: O(|T|) where T is the length of the target string - the recursion will end anyways
    # when the target string exhausts first. In the worse case, we iterate over the entire target string
    
    # Space Complexity: O(|T|)



            