class Solution:
    def RemoveDuplicatedSortedArray(self, nums: list[int])-> int:
        # define variables - I tried to use what I learned in Java logics
        # to solve this question in Python

        count = reader = 1

        # solve edge case - if nums is 0

        if not nums:
            return 0
        
        while reader < len(nums): # loop through the array before reader reaches the end
            if nums[reader] == nums[reader - 1]: # current is the same as the previous
                count +=1
                if count > 2: # reaches the maximum duplicated count
                    nums.pop(reader) # remove the current element
                    reader -= 1 # reader index removed by 1
                    count -= 1

            else:
                count = 1 # reset counter if the current is unique
            reader += 1 # reader pointer moves forward

        # return the new list length
        return len(nums)

'''
Time Complexity: O(n^2) because each deletion takes O(n) and the worst case is all elements are the same,
which is n - 2 deletion. Hence, the time complexity is O(n)+O(n^2) = O(n^2)
Space Complexity: O(1)
'''