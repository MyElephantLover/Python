# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # strategy: maintain a stack which stores indices of days which warmer temperatures not yet found
        # stack stores indices of temperature in decreasing order (top is the most recent smaller temp)
        n = len(temperatures)
        answer = [0] * n
        stack = [] # stores indices
        for i in range(n): # i is from 0 to n - 1
            # while current temp is warmer than stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # if today (i) is warmer than the day at the top of the stack
                # then it is the answer for that earlier day
                prev_index = stack.pop()
                # prev_index = earlier day, i is the warmer future day
                answer[prev_index] = i - prev_index # days waited = i - prev_index
                # i is always the current scanning day
                # stack[-1] is always the earlier unresolved colder day

            stack.append(i) # we only push the current day after we finished resolving 
            # all earlier days this temp can satisfy

        return answer

        
# Time: O(n) each index is pushed once, and pop at most once -> total stack operations 
# across the whole loop is <= 2n -> O(n)
# Space: O(n) stack can hold up to n indices at the worst case