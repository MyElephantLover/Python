# Given:

# logs = [
#     "ERROR Disk full",
#     "INFO Service started",
#     "WARN Retry attempt",
#     "ERROR Timeout"
# ]

# Return:

# {"ERROR": 2, "INFO": 1, "WARN": 1}


# Intuition: given an array, return a hash map with key words and its corresponding frequency

from typing import Dict, List
class Solution:
    def countLogLevels(self, logs: List[str]) -> Dict[str , int]:
        count = {}
        for log in logs:
            parts = log.split()
            if len(parts) == 0: # prevent crash - if parts is empty, no key to retrieve
                continue
            level = parts[0]
            count[level] = count.get(level, 0) + 1
        return count
    
# Time: O(n) where n is the number of logs, and k is the average length for each log string; because log size is 
# bounded and small, we just say O(n)
# Space: O(n) let m equals to the number of log levels, e.g. ERROR, WARN, in the worst case, each log has 
# a unique log level, let m ~ n


    
