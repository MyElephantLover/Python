# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.

class Solution:
    def checkPangram(self, sentence: str) -> bool:
        # a pangram must contain exactly 26 unique English letters
        dic = {} # initialize a dic to store the pair of {value, freq}

        # add values to dic
        for c in sentence:
            dic[ch] = dic.get(ch, 0) + 1 # this line means the value of ch is the freq of ch, and 0 if not seen

        return len(dic) == 26

# Time Complexity: O(n) as we traverse the string once
# Space Complexity: O(1) the maximum space used would be 26


## More Pythonic Solution ##

class Solution:
    def checkPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
    
# set(sentence) automatically removes duplicates

# Time Complexity: O(n) Python must read each character in the sentence to hash it and insert into the set
# Space Complexity: O(1)

