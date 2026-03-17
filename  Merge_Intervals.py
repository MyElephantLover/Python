# Problem:
#  Merge overlapping time intervals:
# [(1,3), (2,4)] → [(1,4)]

class Solution:
    def mergeIntervals(self, intervals: List[tuple]) -> List[tuple]:
        if not intervals:
            return []
        
        # step 1: sort by start time
        intervals.sort(key = lambda x: x[0]) # sort intervals based on the start value

        merged = [intervals[0]] # take the first interval as your starting point

        # step2: iterate through intervals
        for start, end in intervals[1:]:
            last_start, last_end = merged[-1]

            if start <= last_end:
                # overlap -> merge
                merged[-1] = (last_start, max(end, last_end))
            # no overlap -> add new interval
            else:
                merged.append((start, end))

        return merged
    
# Time: O(n log n) due to sorting. n is the number of intervals in the list
# Space: O(n) as we created a merged list




        


