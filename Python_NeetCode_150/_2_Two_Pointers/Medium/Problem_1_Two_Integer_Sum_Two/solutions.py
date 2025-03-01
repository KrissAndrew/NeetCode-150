# Input
# 'numbers': list[int] - sorted in non-decreasing order.
# 'target': int 
# Return
# 'result': list[int] - [index1, index2] indices (1-indexed) of two numbers
# two numbers must add up to target. 
# index1 < index2.

# Solution must use O(1) additional space.
#! This indicates that you may not introduce any new data structures

def two_sum(numbers: list[int], target: int) -> list[int]:
    if not numbers:
        return []
    
    left, right = 0, len(numbers) - 1
    while left < right:
        two_sum = numbers[left] + numbers[right]
    
        if two_sum == target:
            return [left + 1, right + 1]

        if two_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
    