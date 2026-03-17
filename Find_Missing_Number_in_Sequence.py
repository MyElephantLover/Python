# Problem:
#  Given [1,2,3,5], return 4.


class Solution:
    def find_missing_number(self, nums: List[int]) -> int:
        n = len(nums) + 1
        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual
        

# Time: O(n) for n is the length of the list
# Space: O(1) we use arithmetic sum formula to achieve O(1) space