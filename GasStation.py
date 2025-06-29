class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int])-> int:
        total_gain = curr_gain = answer = 0

        for i in range(len(gas)):
            curr_gain += gas[i] - cost[i] # net change in gas
            total_gain += gas[i] - cost[i]

            if curr_gain < 0: # start with 0 initial gas, we need to check if the next position is the valid
                # starting position
                # reset curr_gain to 0
                curr_gain = 0
                answer = i + 1 # start with the next position

        if total_gain < 0:
            return -1
        return answer
    # we start our journey from i = 0 and verify if 0 is a valid starting position by accumulating gas
    # gain[i] at each station along the way
    # Having two valid starting positions contradict the statement given in the problem. Therefore, we only
    # need to consider if station 0 is valid because station 1 is guaranteed not to be valid 
    
    # Time Complexity: O(n)
    # Space Complexity: O(1) we don't need to create a separate gain array. instead, we can calculate 
    # the gas gained for each station as we iterate through them. This way, we avoid the need for additional 
    # space of size O(n)