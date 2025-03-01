# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

def longest_consecutive_sequence(nums: list[int]) -> int:
    if not nums: return 0
    longest = 0
    num_set = set(nums)

    for num in nums:
        if num - 1 not in num_set: # no prior number means start of sequence
            streak = 1
            
            while num + 1 in num_set:
                streak += 1
                num += 1
        
        longest = max(longest, streak)

    return longest


if __name__ == "__main__":
        test_cases = [
             ([2,20,4,10,3,4,5], 4),
             ([0,3,2,5,4,6,1,1], 7),
        ]
    
        print("\nRunning tests for 'Longest Consecutive Sequence'")
        for board, expected in test_cases:
                    assert(longest_consecutive_sequence(board) == expected)