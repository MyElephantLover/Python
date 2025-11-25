def combine_sorted_array(arr1:list[int], arr2:list[int]) -> int:
    ## ans is the array we initiate to store the answer

    ans = []
    # we start at the initial index
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        ## we append the smaller element to the ans array
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
        else:
            ans.append(arr2[j])

    # make sure we exhaust looping through both arrays

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans

# Time Complexity: Since both arr1 and arr2 are sorted, we have to go through each while loop,
# where each while loop is O(n) and O(m) erespectively. Hence, the total time complexity is O(n+m)

# why not O(logn) or O(1): Merging requires a full-scan. At the minimum, we need to "touch" all elements
# in both arrays. Hence, in this question, there is no faster way to do this.

# Space Complexity: O(1) we usually do not count the output as the memory used


