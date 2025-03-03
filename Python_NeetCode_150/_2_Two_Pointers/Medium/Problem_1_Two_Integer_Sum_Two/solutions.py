# Input
# 'numbers': list[int] - sorted in non-decreasing order.
# 'target': int 
# Return
# 'result': list[int] - 
# two numbers must add up to target. 
# index1 < index2.

# Solution must use O(1) additional space.
#! This indicates that you may not introduce any new data structures

def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Summary:
        Processes the sorted list of integers to determine, if any,
        two numbers sum to to the provided target number.

    Parameters:
        numbers (list[int]): A sorted list of integers.
        target (int): interger sum target.

    Returns:
        list[int]: [index1, index2] indices (1-indexed) of two numbers
                   where Index1 < index2.\n Returns an empty list if no
                   valid answer exists.

    Example:
        >>> result = two_sum([1, 2, 3], 5)
        >>> print(result)
        [2, 3]
    """
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
    