# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.

# Constraints:

# 1 <= matches.length <= 105
# matches[i].length == 2
# 1 <= winneri, loseri <= 105
# winneri != loseri
# All matches[i] are unique.

class Solution:
    def players(self, matches: List[List[int]]) -> List[List[[int]]]:
        # initialize variables
        # The hint said count the # of loses while iterating the list
        losses = {} # losses = {loser: number of losses}
        seen = set() # stores all players who played at least one match

        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            if loser not in losses: # first time loser
                losses[loser] = 0
            losses[loser] += 1
        
        zero_loss = []
        one_loss = []
        for player in seen: # this contains both the winner and the loser
            cnt = losses.get(player, 0) # safe dic lookup: d.get(key, default)
            # this line is treating missing as 0
            # if the key exists, return d.get(key), otherwise, return default
            # hashmap.add(), hashmap.remove()
            if cnt == 0:
                zero_loss.append(player)
            elif cnt == 1:
                one_loss.append(player)

        zero_loss.sort()
        one_loss.sort()

        return [zero_loss, one_loss]

# Time Complexity: O(nlogn), the hashset takes O(1) in average, the iteration takes O(n); the sorting takes O(logn)
# Space Complexity: O(n) the maximum size for the set and the hashmap is n

