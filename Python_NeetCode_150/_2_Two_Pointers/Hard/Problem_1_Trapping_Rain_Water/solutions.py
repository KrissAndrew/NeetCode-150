# Given an integer array heights where heights[i] represents the height of the ith bar.
# Return the maximum amount of water that can be contained between the heights.

def trapping_rain_water(heights: list[int]) -> int:
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

if __name__ == "__main__":
        heights = [0,2,0,3,1,0,1,3,2,1]
        result = trapping_rain_water(heights)
        print(result)
