# You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

# A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

# Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

# An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.

# Constraints:

# 1 <= nums1.length, nums2.length <= 105
# 1 <= nums1[i], nums2[j] <= 105
# Both nums1 and nums2 are non-increasing.

class Solution:
    def maxDistanceBetweenAPair(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        max_dist = 0

        while i < len(nums1) and j < len(nums2):
            if i > j:
                j += 1
            elif nums1[i] <= nums2[j]: #satisfy the condition
                max_dist = max(max_dist, j - i)
                j += 1 # we want to maximize (j - i), j += 1 makes the distance bigger
                # this pair is valid, we want to try larger distance
            else:
                # this is invalid pair - meaning i is too big
                # since array is non-increasing, moving i forward can make i smaller
                i += 1

        return max_dist

# Time: O(n + m) where n is the length of nums1 and m is the length of nums2: two pointers: i moves forward at most n times and same for j
# Space: O(1)