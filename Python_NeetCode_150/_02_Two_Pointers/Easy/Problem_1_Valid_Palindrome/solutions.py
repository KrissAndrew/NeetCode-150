# Pythonic and it works, but adds complexity
def valid_palindrome(s: str) -> bool:
    clean_s = ''.join([char.lower() for char in s if char.isalnum()]) # remove all non-alphanumeric items from string whilst lowering
    return clean_s[:len(clean_s) // 2] == clean_s[::-1][:len(clean_s) // 2]

def valid_palindrome(s: str) -> bool:
    clean_s = ''.join([char.lower() for char in s if char.isalnum()]) # remove all non-alphanumeric items from string whilst lowering
    half_way = len(clean_s) // 2
    for i in range(half_way):
        if clean_s[i] != clean_s[len(clean_s) - 1 - i]: return False
    return True

# I can further optimise the function but not creating a clean string, instead iterating pointers when non isalnum() chars are detected
def valid_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        # Move left pointer forward if current character is not alphanumeric.
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer backward if current character is not alphanumeric.
        while right > left and not s[right].isalnum():
            right -= 1
        # Compare the characters in a case-insensitive manner.
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1      
    return True