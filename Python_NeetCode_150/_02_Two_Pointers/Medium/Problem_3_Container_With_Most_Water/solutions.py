# Given an integer array heights where heights[i] represents the height of the ith bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

def max_container(heights: list[int]) -> int:
    """
    Summary:
        Processes the list of integers representing heights to determine the maximum
        spaces between two of the integers representing a container.

    Parameters:
        numbers (list[int]): A list of integers.

    Returns:
        int: Max number of heights possible between provided heights 

    Example:
        >>> result = max_container([1, 7, 2, 5, 4, 7, 3, 6])
        >>> print(result)
        36
        >>> result = max_container([2, 2, 2])
        >>> print(result)
        4
    """
    if not heights:
        return 0
    
    max_volume = 0
    
    # sum of water = height of lower edge (lh) * distance between edges (d)
    left, right = 0, len(heights) - 1
    while left < right:
        left_height, right_height = heights[left], heights[right]
        current_volume = min(left_height, right_height) * (right - left)
        max_volume = max(current_volume, max_volume)

        if left_height <= right_height:
            left += 1
        else:
            right -= 1
            
    return max_volume