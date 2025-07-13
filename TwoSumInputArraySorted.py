class Solution:
    def TwoSumInputSorted(self, numbers: List[int], target: int) -> List[int]:

        # the requirement is 1 <= index1 < index2 < len(numbers)

        low = 0
        high = len(numbers - 1)

        while low < high:
            sum = numbers[low] + numbers[high]

            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1 # move one position to the right
            else:
                high -= 1 # move one position to the left

        # incase there is no solution, return [-1, -1]
        return [-1, -1] 
    
# Follow-Up
# What if the constraint needs us to consider integer overflow?
# In that case, we can cast our data type from int to long before adding them together.
# Casting ensure that we will not get the overflow error since the signed long data type
# supports numbers up to 2^63 - 1. 
# Alternatively, we can check if numbers[low] > (1 << 31) - 1 - numbers[high], this is to check if numbers[low] + numbers[high] will greater than
# (1 << 31) - 1 , aka, a 32-bit signed integer
# (1 << 31) is 2^31, which is 2147483648
# (1 << 31) -1 = 2147483647 which is the maximum value of a 32-bit signed integer
# Hence, we can check if numbers[low] > (1 << 31) - 1 - numbers[high] at the beginning of each iteration to prevent integer overflow

# Time Complexity: O(n)
# Space Complexity: O(1)





