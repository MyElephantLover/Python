class Solution:
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        # Left and Right Product lists - this is the most intuitive approach to me
        n = len(nums)
        answer = n * [0] # create an empty list

        # answer[i] contains the product of all the elements to the left
        # for the element at the index 0, there are no elements to the left
        # the same thing applies for the answer[n - 1], there are no elements to the right of index n - 1

        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # answer[i - 1] contains all the product of the elements to the left of i - 1
        # simply multiplying it with nums[i - 1] would give the product of all the elements to the index i
        # R contains the product of all the elements to the right
        # for the element at the index of n - 1, there are no elements to the right, i.e. it's the last element
        # so the R would be 1

        right = 1
        for i in reversed(range(n)):
            # for the index i, R would contain all the elements to the right
            # we update R accordingly
            answer[i] = answer[i] * right
            right *= nums[i]
        
        return answer

# Time Complexity: O(n)
# Space Complexity: O(n)