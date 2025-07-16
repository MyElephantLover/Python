class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0

        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = left - right
                maxarea = max(maxarea, min(height[left], height[right])* width)
        return maxarea
    
# Use the same logic explained in the Java solution for the same question

# Time Complexity: O(n^2), calculating area for all n(n - 1)/2 height pairs
# Space Complexity: O(1) constant extra space is used

