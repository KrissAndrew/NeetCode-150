# Given an integer array nums
# return all the triplets [nums[i], nums[j], nums[k]]
# nums[i] + nums[j] + nums[k] == 0, all indices (i, j and k) are distinct.
# Output should not contain any duplicate triplets.
# Return the output and the triplets in any order.

def three_sum(numbers: list[int]) -> list[list[int]]:
    """
    Summary:
        Processes the list of integers to determine which, if any,
        combinations of three numbers sum to 0.

    Parameters:
        numbers (list[int]): A list of integers.

    Returns:
        list[list[int]]: [[num1, num2, num3], [num1, num2, num3], ...]
                         Three numbers where num1 != num2 != num3
                         and num1 + num2 + num3 == 0.
                         Returns an empty list if no valid answer exists.

    Example:
        >>> result = three_sum([-1, 0, 1, 2, -1, -4])
        >>> print(result)
        [[-1, -1, 2], [-1, 0, 1]]
    """
    if len(numbers) < 3: # cover lists with 1 or 2 or no items
        return []
    
    numbers = sorted(numbers)
    result = []

    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue
            
        left, right = i + 1, len(numbers) - 1
        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]
            if current_sum == 0:
                result.append([numbers[i], numbers[left], numbers[right]])
                left += 1
                right -= 1
                # Skip duplicates after finding a valid triplet
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result