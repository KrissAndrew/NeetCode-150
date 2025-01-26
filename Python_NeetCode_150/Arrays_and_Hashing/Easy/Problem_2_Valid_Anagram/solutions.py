# Use array and ord to access each item counting letter occurances O(n)
# ord(letter): returns the Unicode code representation of a character.
# Example: ord('a') will return 97.
# Subtracting ord(a) from a lowercase letter gives the alphabetical index for that letter
# ord('a') - ord('a') = 97 - 97 = 0 → index 0 for 'a'
# ord('b') - ord('a') = 98 - 97 = 1 → index 1 for 'b'
# ord('z') - ord('a') = 122 - 97 = 25 → index 25 for 'z'

def valid_anagram(string_one: str, string_two: str) -> bool:
    if len(string_one) != len(string_two): return False

    counter = [0] * 26
    
    for char in string_one.lower():
        counter[ord(char) - ord('a')] += 1
    for char in string_two.lower():
        counter[ord(char) - ord('a')] -= 1

    for val in counter:
        if val != 0: return False
    return True