# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# Constraints:

# n == gain.length
# 1 <= n <= 100
# -100 <= gain[i] <= 100


# For this question, we need to understand two things:
# 1) gain[i] is the net gain on i, and the net altitude gain can be positive or negative
# 2) The altitude at a step can be determined as the altitude at the previous step plus the net gain at the current step
# hence, we can compare the maximum of the previous sum and the current value which is the previous
# sum plus the net gain

class Solution:
    def highest_altitude(self, gain: List[int]) -> int:
        # initialize variables
        curr = 0 # we start at 0
        highest_point = curr # when we start, the highest is the current

        for altitude_gain in gain: # because gain is a list of net gain, can be positive or negative
            curr += altitude_gain # each point the altitude is the net gain plus the previous altitude
            highest_point = max(curr, highest_point)
        
        return highest_point
    
# Time Complexity: O(n) where n is the length of the array gain
# Space Compelxity: O(1) as we only create two variables