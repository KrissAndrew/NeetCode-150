# Given an integer array heights where heights[i] represents the height of the ith bar.
# Return the maximum amount of water that can be contained between the heights.

def trapping_rain_water(heights: list[int]) -> int:
    """
    Calculate the total volume of trapped rain water given a list of tower heights.
    
    Parameters:
        heights (list[int]): A list of non-negative integers representing the heights of towers.
    
    Returns:
        int: The total volume of water that can be trapped.
    """
    if not heights:
        return 0

    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    volume = 0

    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                volume += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                volume += right_max - heights[right]
            right -= 1

    return volume