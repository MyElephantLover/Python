# Problem:
#  Given deployment times for services:
# [2, 4, 3]
# Return how many can be deployed sequentially without delay.

# key idea: check the maximum time seen so far

class Solution:
    def process_deployment(self, times: List[int]) -> int:
        # edge case
        if not times:
            return 0
        
        count = 1 # at least one deployment batch
        curr_max = times[0]

        for t in times[1:]:
            if t <= curr_max:
                # joins current deployment batch
                continue

            else:
                # new deployment batch
                count += 1
                curr_max = t

        return count
    
# Time: O(n) for n is the number of processes
# Space: O(1) as we use constant extra variables

