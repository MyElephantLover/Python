# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# Constraints:

# 1 <= t <= 109
# Each test case will call ping with strictly increasing values of t.
# At most 104 calls will be made to ping.

from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        # add current timestamp
        self.q.append(t)

        # remove timestamp older than t - 3000
        while self.q[0] < t - 3000: # because the queue is sorted by time
            # if removes only one outdated timestamp
            self.q.popleft()

        # remaining elements are within the range
        return len(self.q)
    
# Time: O(1) across all calls, we appended n times, remove n times, so amortised time complexity is O(1)
# Space: O(n) worst case is the n timestamps within 3000 ms

# removing from the front of an array is O(n), if we use an efficient queue to do it,
# it would be O(1)
# bc the call comes in increasing t, so when we add t to the queue, it would be sorted