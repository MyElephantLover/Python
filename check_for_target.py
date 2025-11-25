def check_for_target(num:list[int], target:int) -> bool:
    ## initialize two pointers
    left = 0
    right = len(num) - 1

    while left < right:
        ## we need to set up a current sum, so we can check the current sum against the target
        curr = num[left] = num[right]

        if curr == target:
            return True
        
        ## we start with the left-most and the right-most direction and move inwards
        if curr > target:
            ## meaning the right pointer is no use since it's adding the smallest element, so we need to move to the left
            right -= 1
        # otherwise, meaning the sum is smaller than target, then we need to move the left pointer to the right
        else:
            left += 1

    # if we run through the entire operation, and did not find anything, we need to return False
    return False

## Time Complexity: O(n), the question states this is a sorted array. In the best case, we could get O(1),
## in the worst case that we have to go through the entire array, the time complexity is O(n)
## Space Complexity: O(1) we did not use extra memeory to store the output




