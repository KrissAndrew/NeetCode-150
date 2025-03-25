# Given two strings, s1 and s2, Return true if s2 contains a permutation of s1, or false otherwise.
# That means if a permutation of s1 exists as a substring of s2, then return true.
from collections import Counter

def permutation_in_string(s1: str, s2: str) -> bool:
    char_set = set(s1)
    s2_list = list(s2)
    left, right = 0, len(s1) - 1
    
    counts = Counter(s1) # Initialise a count var if relevant char detected
    
    for i in range(len(s2_list[left:right + 1])):
        if s2_list[i] in char_set:
            counts[s2_list[i]] -= 1 

    while right < len(s2) - 1:

        if all(value == 0 for value in counts.values()):
            return True
        
        if s2_list[left] in char_set: # Add back in lost char
            counts[s2_list[left]] += 1

        left += 1
        right += 1

        if s2_list[right] in char_set:
            counts[s2_list[right]] -= 1

    return all(value == 0 for value in counts.values())

if __name__ == "__main__":
    test_cases = [
        (("a", "a"), True),             #  1 - 'a' is a permutation of 'a'
        (("a", "ab"), True),            #  2 - 'a' is a permutation of '(a)b'
        (("ab", "ba"), True),            #  3 - 'ab' is a permutation of '(ba)'
        (("cb", "abc"), True),          #  3 - 'cb' is a permutation of 'a(bc)'
        (("adc", "dcda"), True),        #  4 - 'adc' is a permutation of 'd(cda)'
        (("abc", "lecabee"), True),     #  5 - 'abc' is a permutation of 'le(cab)ee'
        (("abc", "lecaabee"), False), #  6 - 'abc' is not a permutation of 'lecaabee'
    ]

    all_passed = True
    for idx, (input, expected) in enumerate(test_cases, start=1):
            result = permutation_in_string(*input)
            if result != expected:
                all_passed = False
                print(result, expected, f"Test case {idx}: input={input}, expected={expected}, result {result}")
    if all_passed:
        print("No failures detected.")