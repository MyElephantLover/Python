# Input:

# config = [
#     "host=db.ibm.com",
#     "port=5432",
#     "ssl=true"
# ]

# Return:

# {"host": "db.ibm.com", "port": "5432", "ssl": "true"}

from typing import List, Dict

class Solution:
    def parseKeyValueConfig(self, config: List[str]) -> Dict[str, str]:
        result = {}
        # edge cases
        for line in config:
            if "=" not in line:
                continue # skip current loop iteration and go to the next

            key, value = line.split("=", 1) # string.split(separator, maxofsplit)
            result[key.strip()] = value.strip()

        return result
    
# Time: O(n*k) for n is the number of line in the string and k is the average length of each line
# split(): O(k); strip(): O(k)
# Space: O(n) n is the number of lines

