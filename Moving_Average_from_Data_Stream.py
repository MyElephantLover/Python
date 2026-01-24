# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

# Constraints:

# 1 <= size <= 1000
# -105 <= val <= 105
# At most 104 calls will be made to next.

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.window.append(val) # we only add one new value each time next() being called
        self.window_sum += val

        # reomve oldest value if window exceeds size
        if len(self.window) > self.size:
            removed = self.window.popleft()
            self.window_sum -= removed
        return self.window_sum / len(self.window)
    
# Time: O(1) queue append and pop takes O(1) respectively; O(1) per next() call
# Space: O(size) because it does not grow with the number of calls
