# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

def longest_repeating_char_replacement(s: str, k: int) -> int:
    if len(set(s)) == len(s): # If all characters in string are unique, then replacement is irrelivent
         return 1 + k
    
    result = 0




    return result
         

if __name__ == "__main__":
    test_cases = [
        (("ABA", 1), 3),     #  1 - Can replace one for "AAA" = len 3
        (("XYYX", 2), 4),    #  1 - Can replace two for "XXXX" = len 4
        (("XYYX", 1), 3),    #  1 - Can replace one for "X(YYY)"|"(YYY)X" = len 3
        (("AAABABB", 1), 5), #  2 - Can replace one for "(AAAAA)BB" = len 5
        (("AAABABB", 2), 6), #  2 - Can replace Two for "(AAAAAA)B" = len 5 
    ]

    all_passed = True
    for idx, (input, expected) in enumerate(test_cases, start=1):
            result = longest_repeating_char_replacement(*input)
            if result != expected:
                all_passed = False
                print(result, expected, f"Test case {idx}: input={input}, expected={expected}, result {result}")
    if all_passed:
        print("No failures detected.")