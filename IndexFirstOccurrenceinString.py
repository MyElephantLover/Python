class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        m = len(needle)
        n = len(haystack)

        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start
        return -1
    
# Time Complexity: O(m*n) for every window_start, we may have to iterate at most m times.
# There are n - m + 1 such window_start's. Thus, it is O((n - m + 1)*m), so it is O(n * m)
# Space Complexity: O(1) 
            