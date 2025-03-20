# Given a string, s, and an int, k, find the length of the longest substring of duplicate characters.
# You may replace k characters any uppercase char to lengthen substring.

def longest_repeating_char_replacement(s: str, k: int) -> int:
    s_list = list(s)
    s_len = len(s)
    if len(set(s)) == s_len: # If all characters in string are unique, then replacement is irrelivent
         return 1 + k
    
    if k >= s_len: # If k covers the entire string then the longest 
         return s_len
    
    left, right = 0, 1

    while s_list[left] != s_list[right]:
         left += 1

    return result
         

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