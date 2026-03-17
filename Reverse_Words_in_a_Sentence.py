# Problem:
#  "IBM is great" → "great is IBM"

# reverse the order of words, not characters

class Solution:
    def reverse_words_in_sentence(self, s:str) -> str:
        words = s.split()
        words.reverse()

        return " ".join(words)
    
# Time: O(n) for n is the length of the input string
# Space: O(n) as s.split() creates a new list of words; " ".join(words) create a new string
# strings are immutable - Python must create new memory
    

# cleaner solution

class Solution:
    def reverse_words(self, s: str) -> str:
        return " ".join(s.split()[::-1])
