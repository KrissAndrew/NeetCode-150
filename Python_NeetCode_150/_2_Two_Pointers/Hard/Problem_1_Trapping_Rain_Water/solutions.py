# Given an integer array heights where heights[i] represents the height of the ith bar.
# Return the maximum amount of water that can be contained between the heights.

def trapping_rain_water(heights: list[int]) -> int:
    if not heights:
        return 0

    volume = 0
    max_height = max(heights)

    # Process towers row by row from max heights down to 1.
    for level in range(max_height, 0, -1):
        first = False
        count = 0
        for h in heights:
            if h >= level:
                if first:
                    volume += count
                    count = 0
                first = True
            else:
                if first:
                    count += 1
    return volume

if __name__ == "__main__":
        heights = [0,2,0,3,1,0,1,3,2,1]
        # answer is 9
        result = trapping_rain_water(heights)
        print(result)

        heights = [0,1,0,1,0]
        # answer is 9
        result = trapping_rain_water(heights)
        print(result)