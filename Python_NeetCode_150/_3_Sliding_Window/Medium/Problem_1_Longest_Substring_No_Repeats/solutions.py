# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

def longest_non_repeat_substring(s: str) -> int:
    if len(s) == 0:
        return 0
    if len(set(s)) == 1:
        return 1
    elif len(s) == 2:
        return 2
     
    s = list(s)
    seen = set()
    p1, p2 = 0, 1
    longest = 1
       
    
    while p2 < len(s) - 1:
        if s[p1] == s[p2]: # Only start counting numbers following duplicates
            p1 += 1
            p2 += 1
        seen.add(s[p1])
        while s[p2] not in seen and p2 < len(s) - 1:
            seen.add(s[p2])
            p2 += 1
            longest = max(p2 - p1, longest)
        p1 = p2
        p2 += 1
        seen = set()

    return longest
         
     



if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),          # max profit is 6 - 1 = 5
        ("zxyzxyz", 3),       # max profit is 7 - 3 = 4
        ("xxxx", 1),          # max profit is 6 - 1 = 5
        ("aabbcc", 2),       # max profit is 6 - 1 = 5
    ]


    for idx, (string, expected) in enumerate(test_cases, start=1):
            result = longest_non_repeat_substring(string)
            if result != expected:
                print(result, expected, f"Test case {idx}: string={string}, expected={expected}, result {result}")