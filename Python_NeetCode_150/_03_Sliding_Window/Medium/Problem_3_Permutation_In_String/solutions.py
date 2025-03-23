# Given two strings, s1 and s2, Return true if s2 contains a permutation of s1, or false otherwise.
# That means if a permutation of s1 exists as a substring of s2, then return true.
from collections import Counter

def permutation_in_string(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    
    char_set = set(s1)
    s2_list = list(s2)
    left, right = 0, 1

    while left < len(s2_list):
        c = s2_list[left]
        right = left + 1 # begin checking from next char onwards
        if c in char_set:
            counts = Counter(s1) # Initialise a count var if relevant char detected
            counts[c] -= 1 # Decrement current count
            while right < len(s2):
                if all(value == 0 for value in counts.values()):
                    return True
                char = s2_list[right]
                if char in char_set and counts[char] > 0:
                    counts[char] -= 1
                    right += 1
                else: # char not in set, not permutation. move on
                    break
        left = right
                 
    return False
         

if __name__ == "__main__":
    test_cases = [
        # (("a", "a"), True),           #  1 - 'a' is a permutation of 'a'
        # (("a", "ab"), True),          #  2 - 'a' is a permutation of '(a)b'
        # (("cb", "abc"), True),        #  3 - 'cb' is a permutation of 'a(bc)'
        # (("adc", "dcda"), True),        #  1 - 'adc' is a permutation of 'd(cda)'
        # (("abc", "lecabee"), True),   #  3 - 'abc' is a permutation of 'le(cab)ee'
        # (("abc", "lecaabee"), False), #  3 - 'abc' is not a permutation of 'lecaabee'
    ]

    all_passed = True
    for idx, (input, expected) in enumerate(test_cases, start=1):
            result = permutation_in_string(*input)
            if result != expected:
                all_passed = False
                print(result, expected, f"Test case {idx}: input={input}, expected={expected}, result {result}")
    if all_passed:
        print("No failures detected.")