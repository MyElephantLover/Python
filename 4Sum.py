from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
        # Skip duplicate numbers for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):
            # Skip duplicate numbers for j
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])

                    # Move past duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return res
