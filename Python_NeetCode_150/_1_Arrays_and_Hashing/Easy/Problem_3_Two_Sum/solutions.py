# Given an array of integers 'nums' and an integer 'target', return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

# O(n)

def two_sum(nums: list[int], target: int) -> list[int]:
    number_indices = {}

    for i in range(len(nums)):
        difference = target - nums[i]
        if (difference in number_indices): return [number_indices[difference], i]
        number_indices[nums[i]] = i
    
    return []