# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

def longest_non_repeat_substring(s: str) -> int:
    length = len(s)
    if length == 0:
        return 0

    seen = {}
    longest = 0
    start = 0

    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            # Update longest before shifting start if needed
            longest = max(longest, i - start)
            start = seen[char] + 1
        seen[char] = i
    # Check for the last window
    longest = max(longest, length - start)
    return longest
         

if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3), #  1
        ("zxyzxyz", 3),  #  2
        ("xxxx", 1),     #  3
        ("aabbcc", 2),   #  4
        ("abcabcbb", 3), #  5
        ("au", 2),       #  6
        ("aab", 2),      #  7
    ]

    all_passed = True
    for idx, (string, expected) in enumerate(test_cases, start=1):
            result = longest_non_repeat_substring(string)
            if result != expected:
                all_passed = False
                print(result, expected, f"Test case {idx}: string={string}, expected={expected}, result {result}")
    if all_passed:
        print("No failures detected.")