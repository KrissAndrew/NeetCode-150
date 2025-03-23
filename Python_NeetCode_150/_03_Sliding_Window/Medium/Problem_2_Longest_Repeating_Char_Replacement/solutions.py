# Given a string, s, and an int, k, find the length of the longest substring of duplicate characters.
# You may replace k characters any uppercase char to lengthen substring.

def longest_repeating_char_replacement(s: str, k: int) -> int:
    count = {}
    max_count = 0  # max frequency in the current window
    max_length = 0
    left = 0

    for right in range(len(s)):
        # Update the frequency count for the current character
        count[s[right]] = count.get(s[right], 0) + 1
        
        # Update the maximum frequency seen in the current window
        max_count = max(max_count, count[s[right]])
        
        # If the number of chars to replace exceeds k, shrink the window from the left
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        
        # Update the maximum window size
        max_length = max(max_length, right - left + 1)
    
    return max_length
         

if __name__ == "__main__":
    test_cases = [
        (("ABC", 1), 2),     #  1 - Can replace one for "(AA)C"|"A(BB)"|"A(CC)" = len 3
        (("ABA", 1), 3),     #  1 - Can replace one for "(AAA)" = len 3
        (("XYYX", 1), 3),    #  1 - Can replace one for "X(YYY)"|"(YYY)X" = len 3
        (("XYYX", 2), 4),    #  1 - Can replace two for "(XXXX)" = len 4
        (("AAABABB", 1), 5), #  2 - Can replace one for "(AAAAA)BB" = len 5
        (("AAABABB", 2), 6), #  2 - Can replace Two for "(AAAAAA)B" = len 6
    ]

    all_passed = True
    for idx, (input, expected) in enumerate(test_cases, start=1):
            result = longest_repeating_char_replacement(*input)
            if result != expected:
                all_passed = False
                print(result, expected, f"Test case {idx}: input={input}, expected={expected}, result {result}")
    if all_passed:
        print("No failures detected.")