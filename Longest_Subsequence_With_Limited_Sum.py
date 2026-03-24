# You are given an integer array nums of length n, and an integer array queries of length m.

# Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# Constraints:

# n == nums.length
# m == queries.length
# 1 <= n, m <= 1000
# 1 <= nums[i], queries[i] <= 106

# Idea: to maximize the subsequence size under a sum limit, you should always take the smallest element first

from typing import List
import bisect

class Solution:
    def longestSequence(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        # queries.sort() # we wanted to return answer in the original query order
        answer = []
        n = len(nums)
        m = len(queries)

        # build prefix sums
        prefix = []
        total = 0 # sum limit
        for num in nums:
            total += num
            prefix.append(total)

        # for each query, find how many prefix sums are <= total
        answer = []
        for q in queries:
            count = bisect.bisect_right(prefix, q) # bisect_right() returns the number of elements in array which are <= x
            # we need to find the largest index i such that prefix[i] <= q
            answer.append(count)

        return answer

# Time: O(nlogn + mlogm) for one sort in nums and a binary search in queries
# Space: O(n + m) for the array answer with length as m, and prefix array with length as n



