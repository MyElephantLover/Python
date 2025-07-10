class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Approach 1: Compare with Reverse

        # Remove all non-alphanumeric characters

        filtered_chars = filter(lambda ch: ch.isalnum(), s) # lambda ch: ch.isalnum() is a short function which 
        # return True if the characters ch is alphanumetric

        # change to lowercase

        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1] # [::-1] is a slice operation that returns a reversed
        # copy of the list

        return filtered_chars_list == reversed_chars_list
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)







