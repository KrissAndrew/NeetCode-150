# Given an integer array heights where heights[i] represents the height of the ith bar.
# Return the maximum amount of water that can be contained between the heights.

def trapping_rain_water(heights: list[int]) -> int:
    if not heights or len(heights) < 3: # Sizes below 3 cannot hold water beween
        return 0

    trapped = 0
    counter = 0
    left, right = 1, 2



    while left != len(heights) and right < len(heights):
        left_height, right_height = heights[left], heights[right] 
        while right_height < left_height:
             right += 1
             right_height = heights[right]
        if left == right: right += 1
        while left != right and right < len(heights):
             prev_peak = left_height
             left += 1
             left_height = heights[left]
             trapped += prev_peak - left_height
             
    return trapped

if __name__ == "__main__":
        heights = [0,2,0,3,1,0,1,3,2,1]
        # answer is 9
        result = trapping_rain_water(heights)
        print(result)

        heights = [0,1,0,1,0]


