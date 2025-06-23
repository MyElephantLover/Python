class Solution:
    def jump(self, nums: List[int])-> int:

        # The starting range of the fist jump is [0,0]
        # The format of the jump is [end, far] where end being the farthest starting index, and far being the farthest index it can reach
        # in short, if we can reach to the farthest index with the least jumps, say, i,  we will not go for more than i jumps

        cur_end = cur_far = 0
        n = len(nums)

        for i in range(n - 1):
            # update the farthest reachable index in this jump
            curFar = max(curFar, i + nums[i])

            # if we finish the starting range of this jump
            # move on to the next jump

            if i == cur_end:
                answer +=1
                cur_end = cur_far

        return answer

# Time Complexity: O(n) we iterate over n and reach to the second last element. In each iteration, we do some calculations which takes constant time
# Space Complexity: O(1)


            
