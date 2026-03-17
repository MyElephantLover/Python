# Return:

# 1 if version A > version B

# -1 if version A < version B

# 0 if equal

# Examples:

# "1.2.10" vs "1.2.3" → 1

# "2.0" vs "2.0.0" → 0


class Solution:
    def compare_two_version_strings(self, s: str, t: str) -> int:
        v1 = [int(x) for x in s.split(".")]
        v2 = [int(y) for y in t.split(".")]

        # make both lists the same length
        # in versioning, missing values are treated as 0
        # 2.0 = 2.0.0 = 2.0.0.0
        max_length = max(len(v1), len(v2)) 
        v1 += [0] * (max_length - len(v1))
        v2 += [0] * (max_length - len(v2))

        # compare each part
        for a, b in zip(v1, v2): # zip will compare all parts
            if a > b:
                return 1
            elif a < b:
                return -1
                
        return 0 # only after checking everyhing
    
# Time: O(n + m) where n, m is the number of version segments in each string
# Space: O(n + m) for the two lists of parsed version segments
            
