from typing import List
# Given an array of integers 'nums' and an integer 'target', return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.


# O(n^2) - nested for loops
def two_sum_v1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target: return [i, j]

# O(n)

def two_sum(nums: List[int], target: int) -> List[int]:
    number_indices = {}

    for i in range(len(nums)):
        difference = target - nums[i]
        if (difference in number_indices): return [number_indices[difference], i]
        number_indices[nums[i]] = i
    
    return []